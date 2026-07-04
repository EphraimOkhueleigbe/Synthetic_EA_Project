def add_retracement(df):

    retracement = []


    for i in range(len(df)):


        trend = df["Trend"].iloc[i]

        high = df["High"].iloc[i]

        low = df["Low"].iloc[i]

        ema9 = df["EMA_9"].iloc[i]



        touched = False



        # bullish retracement

        if trend == 1:

            if low <= ema9:

                touched = True



        # bearish retracement

        elif trend == -1:

            if high >= ema9:

                touched = True



        retracement.append(touched)



    df["Retracement"] = retracement


    return df