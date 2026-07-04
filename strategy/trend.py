import pandas as pd


def add_trend(df):

    trend = []

    current_trend = 0


    for i in range(len(df)):


        if i == 0:

            trend.append(current_trend)

            continue



        previous_fast = df["EMA_9"].iloc[i-1]
        previous_slow = df["EMA_18"].iloc[i-1]


        current_fast = df["EMA_9"].iloc[i]
        current_slow = df["EMA_18"].iloc[i]



        bullish_cross = (
            previous_fast <= previous_slow
            and
            current_fast > current_slow
        )


        bearish_cross = (
            previous_fast >= previous_slow
            and
            current_fast < current_slow
        )



        if bullish_cross:

            current_trend = 1



        elif bearish_cross:

            current_trend = -1



        trend.append(current_trend)



    # convert list to pandas Series

    trend = pd.Series(
        trend,
        index=df.index
    )


    # shift trend activation to next candle

    df["Trend"] = (
        trend.shift(1)
        .fillna(0)
        .astype(int)
    )


    return df