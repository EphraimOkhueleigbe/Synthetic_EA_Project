import MetaTrader5 as mt5
import pandas as pd

def connect_mt5():
    if not mt5.initialize():
        print("MT5 initialization failed")
        print(mt5.last_error())
        return False

    print("MT5 connected successfully")
    return True

def get_candles(symbol, timeframe, amount):
    if not mt5.symbol_select(symbol, True):
        print(f"Cannot select {symbol}")
        return None

    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe,
        0,
        amount
    )

    if rates is None:
        print("No data returned")
        return None

    df = pd.DataFrame(rates)

    df["time"] = pd.to_datetime(
        df["time"],
        unit="s"
    )

    df.set_index(
        "time",
        inplace=True
    )

    df.rename(
        columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close"
        },
        inplace=True
    )

    return df[
        [
            "Open",
            "High",
            "Low",
            "Close"
        ]
    ]
