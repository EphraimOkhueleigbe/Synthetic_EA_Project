trade_history = []


def save_trade(trade, result):

    completed_trade = {

        "direction": trade["direction"],

        "entry": trade["entry"],

        "exit": result["exit"],

        "entry_time": trade.get("entry_time"),

        "exit_time": result["time"],

        "stop_loss": trade["stop_loss"],

        "take_profit": trade["take_profit"],

        "lot_size": trade["lot_size"],

        "result": result["result"]

    }

    trade_history.append(completed_trade)


def get_history():

    return trade_history