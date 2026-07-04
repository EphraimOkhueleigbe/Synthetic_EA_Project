trade_history = []


def save_trade(trade, result):

    trade_history.append({

        **trade,

        **result

    })


def get_history():

    return trade_history