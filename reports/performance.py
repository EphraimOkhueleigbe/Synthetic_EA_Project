from typing import List
from backtester.models import Trade

def performance_report(history: List[Trade], starting_balance: float = 1000.0):
    total_trades = len(history)
    wins = 0
    losses = 0
    closed_by_trend = 0
    
    gross_profit = 0.0
    gross_loss = 0.0
    
    balance = starting_balance
    max_balance = balance
    max_drawdown = 0.0
    
    for trade in history:
        # Skip open trades
        if trade.result == "OPEN":
            continue
            
        pnl = trade.pnl
        balance += pnl
        
        if pnl > 0:
            wins += 1
            gross_profit += pnl
        else:
            losses += 1
            gross_loss += abs(pnl)
            
        if trade.result == "CLOSED_BY_TREND":
            closed_by_trend += 1
            
        # Drawdown tracking
        if balance > max_balance:
            max_balance = balance
        
        drawdown = max_balance - balance
        if drawdown > max_drawdown:
            max_drawdown = drawdown
            
    closed_trades = wins + losses
    win_rate = (wins / closed_trades * 100) if closed_trades > 0 else 0.0
    net_profit = balance - starting_balance
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else (float("inf") if gross_profit > 0 else 1.0)
    
    print("\n" + "=" * 50)
    print("BACKTEST PERFORMANCE REPORT (ACTUAL METRICS)")
    print("=" * 50)
    print(f"Starting Balance  : ${starting_balance:.2f}")
    print(f"Ending Balance    : ${balance:.2f}")
    print(f"Net Profit        : ${net_profit:.2f}")
    print(f"Max Drawdown      : ${max_drawdown:.2f}")
    print(f"Profit Factor     : {profit_factor:.2f}")
    print()
    print(f"Total Trades      : {closed_trades}")
    print(f"Wins              : {wins}")
    print(f"Losses            : {losses}")
    print(f"Closed by Trend   : {closed_by_trend}")
    print(f"Win Rate          : {win_rate:.2f}%")
    print()
    print(f"Gross Profit      : ${gross_profit:.2f}")
    print(f"Gross Loss        : ${gross_loss:.2f}")
    print("=" * 50)
