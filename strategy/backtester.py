from strategy.trade_manager import create_trade
from strategy.exit_manager import check_trade_exit


def run_backtest(daily, m30, starting_balance):

    balance = starting_balance

    trade_history = []

    # Stores when the previous trade closed
    trade_end_time = None

    for index, row in daily.iterrows():

        # -------------------------------------------------
        # Skip D1 candles while previous trade is active
        # -------------------------------------------------

        if trade_end_time is not None and index <= trade_end_time:
            continue

        signal = row["Signal"]

        if signal == "NONE":
            continue

        # -------------------------------------------------
        # Create Trade
        # -------------------------------------------------

        trade = create_trade(

            signal,

            row["Close"],

            row["High"],

            row["Low"],

            balance

        )

        # Only M30 candles after the trade opens

        future_m30 = m30[
            m30.index > index
        ]

        result = check_trade_exit(
            trade,
            future_m30
        )

        trade["result"] = result

        trade_history.append(trade)

        # -------------------------------------------------
        # Remember when the trade closed
        # -------------------------------------------------

        if result["result"] != "OPEN":
            trade_end_time = result["time"]
        else:
            # Trade never closed before the dataset ended
            break

    return trade_history