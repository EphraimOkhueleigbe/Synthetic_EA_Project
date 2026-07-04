import pandas as pd


def export_trades(history, filename="trade_history.csv"):

    rows = []

    for trade in history:

        rows.append({
            "Direction": trade["direction"],
            "Entry": trade["entry"],
            "StopLoss": trade["stop_loss"],
            "TakeProfit": trade["take_profit"],
            "LotSize": trade["lot_size"],
            "Result": trade["result"]["result"],
            "Exit": trade["result"]["exit"],
            "ExitTime": trade["result"]["time"]
        })

    df = pd.DataFrame(rows)

    df.to_csv(filename, index=False)

    print(f"\nTrade history saved to {filename}")