class SignalGenerator:

    BUY = "BUY"
    SELL = "SELL"
    NONE = None

    @staticmethod
    def ema_crossover(
        fast_previous,
        slow_previous,
        fast_current,
        slow_current,
    ):

        # BUY

        if (
            fast_previous <= slow_previous
            and
            fast_current > slow_current
        ):
            return SignalGenerator.BUY

        # SELL

        if (
            fast_previous >= slow_previous
            and
            fast_current < slow_current
        ):
            return SignalGenerator.SELL

        return SignalGenerator.NONE