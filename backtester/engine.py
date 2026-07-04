import pandas as pd
import numpy as np
import datetime
from typing import List, Optional
from backtester.models import Trade

def run_backtest(daily: pd.DataFrame, m30: pd.DataFrame, starting_balance: float) -> List[Trade]:
    balance = starting_balance
    trade_history: List[Trade] = []
    
    # Active state variables
    current_trade: Optional[Trade] = None
    waiting_for_confirmation = False
    active_direction = 0
    retrace_high = 0.0
    retrace_low = 0.0
    
    # To track daily date changes
    last_date: Optional[datetime.date] = None
    
    # Pre-calculate yesterday's daily candle index for each M30 candle to avoid slow filtering
    # daily.index and m30.index must be sorted datetime indexes
    daily_times = daily.index.values
    m30_normalized_times = m30.index.normalize().values
    
    # np.searchsorted(..., side='left') - 1 gives the index of the daily candle that closed before today
    yesterday_d1_indices = np.searchsorted(daily_times, m30_normalized_times, side='left') - 1
    
    # Crossover flag helper: we look for cross between idx-1 and idx
    for idx in range(1, len(m30)):
        m30_time = m30.index[idx]
        yesterday_idx = yesterday_d1_indices[idx]
        
        # We need a closed daily candle from yesterday to make any decisions
        if yesterday_idx < 0 or yesterday_idx >= len(daily):
            continue
            
        yesterday_row = daily.iloc[yesterday_idx]
        curr_date = m30_time.date()
        
        # ==========================================
        # 1. EVALUATE DAILY DATA (ON NEW DAY OPEN)
        # ==========================================
        if last_date is None or curr_date != last_date:
            last_date = curr_date
            
            # Read daily signals from yesterday's closed candle
            yesterday_trend = int(yesterday_row["Trend_Raw"])
            yesterday_retrace = bool(yesterday_row["Retracement"])
            
            # Trend Change Exit:
            # If we have an open trade, check if the daily trend has become opposite
            if current_trade is not None:
                opposite_trend = (
                    (current_trade.direction == "BUY" and yesterday_trend == -1) or
                    (current_trade.direction == "SELL" and yesterday_trend == 1)
                )
                if opposite_trend:
                    # Exit immediately at the open of the current M30 candle
                    exit_price = m30.iloc[idx]["Open"]
                    current_trade.close(
                        exit_time=m30_time,
                        exit_price=exit_price,
                        result="CLOSED_BY_TREND"
                    )
                    balance += current_trade.pnl
                    trade_history.append(current_trade)
                    current_trade = None
            
            # Trend Change Confirmation Reset:
            # If we are waiting for confirmation and the trend changed, reset the wait state
            if waiting_for_confirmation and yesterday_trend != active_direction:
                waiting_for_confirmation = False
                active_direction = 0
            
            # Trigger New Retracement Waiting State:
            # Only if we don't have an active trade and are not already waiting (or if new retracement updates parameters)
            if current_trade is None and yesterday_retrace:
                waiting_for_confirmation = True
                active_direction = yesterday_trend
                retrace_high = yesterday_row["High"]
                retrace_low = yesterday_row["Low"]
        
        # ==========================================
        # 2. CHECK EXITS FOR ACTIVE TRADE (ON M30)
        # ==========================================
        if current_trade is not None:
            # We check if this candle's price range hit our SL or TP
            m30_high = m30.iloc[idx]["High"]
            m30_low = m30.iloc[idx]["Low"]
            
            if current_trade.direction == "BUY":
                # Check Stop Loss first (conservative)
                if m30_low <= current_trade.stop_loss:
                    current_trade.close(
                        exit_time=m30_time,
                        exit_price=current_trade.stop_loss,
                        result="LOSS"
                    )
                    balance += current_trade.pnl
                    trade_history.append(current_trade)
                    current_trade = None
                # Check Take Profit
                elif m30_high >= current_trade.take_profit:
                    current_trade.close(
                        exit_time=m30_time,
                        exit_price=current_trade.take_profit,
                        result="WIN"
                    )
                    balance += current_trade.pnl
                    trade_history.append(current_trade)
                    current_trade = None
                    
            elif current_trade.direction == "SELL":
                # Check Stop Loss first (conservative)
                if m30_high >= current_trade.stop_loss:
                    current_trade.close(
                        exit_time=m30_time,
                        exit_price=current_trade.stop_loss,
                        result="LOSS"
                    )
                    balance += current_trade.pnl
                    trade_history.append(current_trade)
                    current_trade = None
                # Check Take Profit
                elif m30_low <= current_trade.take_profit:
                    current_trade.close(
                        exit_time=m30_time,
                        exit_price=current_trade.take_profit,
                        result="WIN"
                    )
                    balance += current_trade.pnl
                    trade_history.append(current_trade)
                    current_trade = None
        
        # ==========================================
        # 3. CHECK ENTRIES (ON M30)
        # ==========================================
        # Only check entries if we don't have an active trade and are waiting for confirmation
        if current_trade is None and waiting_for_confirmation:
            prev_fast = m30.iloc[idx-1]["EMA_9"]
            prev_slow = m30.iloc[idx-1]["EMA_18"]
            curr_fast = m30.iloc[idx]["EMA_9"]
            curr_slow = m30.iloc[idx]["EMA_18"]
            
            crossover_occurred = False
            trade_direction = ""
            
            # BUY Confirmation: EMA 9 crosses above EMA 18
            if active_direction == 1:
                if prev_fast <= prev_slow and curr_fast > curr_slow:
                    crossover_occurred = True
                    trade_direction = "BUY"
                    
            # SELL Confirmation: EMA 9 crosses below EMA 18
            elif active_direction == -1:
                if prev_fast >= prev_slow and curr_fast < curr_slow:
                    crossover_occurred = True
                    trade_direction = "SELL"
            
            if crossover_occurred:
                # We enter on the Open price of the NEXT M30 candle
                if idx < len(m30) - 1:
                    entry_idx = idx + 1
                    entry_time = m30.index[entry_idx]
                    entry_price = m30.iloc[entry_idx]["Open"]
                    
                    if trade_direction == "BUY":
                        stop_loss = retrace_low - 5.0
                        take_profit = entry_price + 500.0
                    else:  # SELL
                        stop_loss = retrace_high + 12.5
                        take_profit = entry_price - 500.0
                    
                    # Risk-based lot sizing can go here; using user's standard model:
                    lot_size = balance * 0.0008
                    
                    current_trade = Trade(
                        direction=trade_direction,
                        entry_time=entry_time,
                        entry_price=entry_price,
                        stop_loss=stop_loss,
                        take_profit=take_profit,
                        lot_size=lot_size
                    )
                    
                    # Crossover consumed, stop waiting
                    waiting_for_confirmation = False
                    active_direction = 0
                    
    return trade_history
