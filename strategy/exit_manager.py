def check_trade_exit(trade, m30):


    entry = trade["entry"]

    stop = trade["stop_loss"]

    target = trade["take_profit"]

    direction = trade["direction"]



    for index,row in m30.iterrows():


        high = row["High"]

        low = row["Low"]



        if direction == "BUY":


            if low <= stop:

                return {
                    "result":"LOSS",
                    "exit":stop,
                    "time":index
                }



            if high >= target:

                return {
                    "result":"WIN",
                    "exit":target,
                    "time":index
                }



        if direction == "SELL":


            if high >= stop:

                return {
                    "result":"LOSS",
                    "exit":stop,
                    "time":index
                }



            if low <= target:

                return {
                    "result":"WIN",
                    "exit":target,
                    "time":index
                }



    return {

        "result":"OPEN",

        "exit":None,

        "time":None

    }