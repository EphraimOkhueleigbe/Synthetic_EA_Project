from app.engine.ema import EMA


class TrendDetector:
    """
    Detects trend using two EMA series.
    """

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"

    @staticmethod
    def detect(prices, fast_period, slow_period):

        if len(prices) < max(fast_period, slow_period):
            return TrendDetector.NEUTRAL

        fast = EMA.calculate(prices, fast_period)
        slow = EMA.calculate(prices, slow_period)

        if fast[-1] > slow[-1]:
            return TrendDetector.BULLISH

        if fast[-1] < slow[-1]:
            return TrendDetector.BEARISH

        return TrendDetector.NEUTRAL