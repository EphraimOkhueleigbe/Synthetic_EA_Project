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

from strategy.trade_manager import create_trade

from strategy.exit_manager import check_trade_exit

from strategy.trade_history import (
    save_trade,
    get_history
)


if connect_mt5():

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
    # TRADE SIMULATION
    # =========================

    trade_active = False



    for index, row in daily.iterrows():


        signal = row["Signal"]



        # Ignore new trades while one is active

        if trade_active:

            continue



        if signal != "NONE":


            trade = create_trade(

                signal,

                row["Close"],

                row["High"],

                row["Low"],

                1000

            )



            print("\nNEW TRADE")

            print(trade)



            # Only candles after entry

            future_m30 = m30[
                m30.index > index
            ]



            result = check_trade_exit(

                trade,

                future_m30

            )



            print("\nTRADE RESULT")

            print(result)

            if result["result"] != "OPEN":

                save_trade(
                    trade,
                    result
                )



            # =========================
            # TRADE STATE CONTROL
            # =========================

            if result["result"] == "OPEN":

                trade_active = True

            else:

                trade_active = False




    print("\nD1 TREND DATA")


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

    print("\nTRADE HISTORY\n")

    for trade in get_history():

        print(trade)

    mt5.shutdown()