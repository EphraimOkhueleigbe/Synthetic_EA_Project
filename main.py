import MetaTrader5 as mt5

from settings.config import SYMBOL, D1_CANDLES, M30_CANDLES
from broker.mt5_loader import connect_mt5, get_candles
from strategy.indicators import add_ema
from strategy.trend import add_trend
from strategy.retracement import add_retracement
from backtester.engine import run_backtest
from reports.performance import performance_report
from reports.export import export_trades

def main():
    if not connect_mt5():
        print("MetaTrader 5 connection failed.")
        return

    # =========================
    # LOAD DATA
    # =========================
    print(f"Loading {D1_CANDLES} D1 candles for {SYMBOL}...")
    daily = get_candles(
        SYMBOL,
        mt5.TIMEFRAME_D1,
        D1_CANDLES
    )

    print(f"Loading {M30_CANDLES} M30 candles for {SYMBOL}...")
    m30 = get_candles(
        SYMBOL,
        mt5.TIMEFRAME_M30,
        M30_CANDLES
    )

    if daily is None or m30 is None:
        print("Failed to load historical candles.")
        mt5.shutdown()
        return

    # =========================
    # INDICATORS
    # =========================
    daily = add_ema(daily)
    m30 = add_ema(m30)

    # =========================
    # STRATEGY ENGINE
    # =========================
    daily = add_trend(daily)
    daily = add_retracement(daily)

    # =========================
    # DEBUG SIGNALS
    # =========================
    print("\nDAILY TREND COUNTS")
    print(daily["Trend_Raw"].value_counts())

    print("\nDAILY RETRACEMENT COUNTS")
    print(daily["Retracement"].value_counts())

    print("\nLAST 50 DAILY CANDLES")
    print(
        daily[
            [
                "Close",
                "EMA_9",
                "EMA_18",
                "Trend_Raw",
                "Trend",
                "Retracement"
            ]
        ].tail(50)
    )

    # =========================
    # BACKTEST
    # =========================
    print("\nRunning chronological backtest...")
    history = run_backtest(
        daily,
        m30,
        starting_balance=1000.0
    )

    # =========================
    # RESULTS
    # =========================
    print(f"\nBACKTEST COMPLETED. Total Trades Generated: {len(history)}")
    
    print("\nTRADES LIST:")
    for trade in history:
        # Displaying trade details cleanly
        exit_time_str = trade.exit_time.strftime('%Y-%m-%d %H:%M') if trade.exit_time else "N/A"
        entry_time_str = trade.entry_time.strftime('%Y-%m-%d %H:%M')
        print(
            f"{trade.direction} | Entry: {entry_time_str} @ {trade.entry_price:.2f} | "
            f"Exit: {exit_time_str} @ {trade.exit_price if trade.exit_price else 0.0:.2f} | "
            f"Result: {trade.result} | PnL: ${trade.pnl:.2f}"
        )

    performance_report(
        history,
        starting_balance=1000.0
    )

    export_trades(history)

    mt5.shutdown()

if __name__ == "__main__":
    main()