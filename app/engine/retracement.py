from app.engine.ema import EMA


class RetracementDetector:
    """
    Detects whether price has retraced to the fast EMA.
    """

    @staticmethod
    def touched(prices, period):

        if len(prices) < period:
            return False

        ema = EMA.calculate(prices, period)

        latest_price = prices[-1]
        latest_ema = ema[-1]

        return latest_price <= latest_ema