class EMA:
    """
    Exponential Moving Average calculator.
    """

    @staticmethod
    def calculate(prices, period):
        """
        Returns a list containing EMA values.

        Parameters
        ----------
        prices : list[float]
        period : int

        Returns
        -------
        list
        """

        if period <= 0:
            raise ValueError("Period must be greater than zero.")

        if len(prices) == 0:
            return []

        multiplier = 2 / (period + 1)

        ema = []

        ema.append(prices[0])

        for price in prices[1:]:

            previous = ema[-1]

            current = (price - previous) * multiplier + previous

            ema.append(current)

        return ema