from ta.trend import EMAIndicator

def add_ema(df):
    df["EMA_9"] = EMAIndicator(
        close=df["Close"],
        window=9
    ).ema_indicator()

    df["EMA_18"] = EMAIndicator(
        close=df["Close"],
        window=18
    ).ema_indicator()

    return df
