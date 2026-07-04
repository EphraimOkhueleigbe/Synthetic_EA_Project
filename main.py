import MetaTrader5 as mt5

from config import SYMBOL

from data.mt5_loader import (
    connect_mt5,
    get_candles
)

from indicators.ema import add_ema

from strategy.trend import add_trend
from strategy.retracement import add_retracement
from strategy.confirmation import add_confirmation

from strategy.backtester import run_backtest
from strategy.performance import performance_report

from strategy.export import export_trades

if connect_mt5():

    # =========================
    # LOAD DATA
    # =========================

    daily = get_candles(
        SYMBOL,
        mt5.TIMEFRAME_D1,
        1000
    )

    m30 = get_candles(
        SYMBOL,
        mt5.TIMEFRAME_M30,
        5000
    )

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

    daily = add_confirmation(
        daily,
        m30
    )

    # =========================
    # DEBUG SIGNALS
    # =========================

    print("\nSIGNAL COUNTS")
    print(daily["Signal"].value_counts())

    print("\nLAST 50 DAILY CANDLES")
    print(
        daily[
            [
                "Close",
                "EMA_9",
                "EMA_18",
                "Trend",
                "Retracement",
                "Signal"
            ]
        ].tail(50)
    )

    # =========================
    # BACKTEST
    # =========================

    history = run_backtest(
        daily,
        m30,
        1000
    )

    # =========================
    # RESULTS
    # =========================

    print("\nBACKTEST RESULTS\n")

    for trade in history:
        print(trade)

    performance_report(
        history,
        starting_balance=1000
    )

    performance_report(
        history,
        starting_balance=1000
    )

    export_trades(history)

    mt5.shutdown()