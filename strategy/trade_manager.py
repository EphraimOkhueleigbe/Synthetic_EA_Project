def create_trade(signal, entry, retrace_high, retrace_low, balance):


    if signal == "BUY":

        stop_loss = retrace_low - 5

        take_profit = entry + 500


    elif signal == "SELL":

        stop_loss = retrace_high + 12.5

        take_profit = entry - 500


    else:

        return None



    lot_size = balance * 0.0008


    return {

        "direction": signal,

        "entry": entry,

        "stop_loss": stop_loss,

        "take_profit": take_profit,

        "lot_size": lot_size

    }