class EAContext:

    def __init__(self):

        self.trend = 0

        self.waiting_for_retracement = False

        self.waiting_for_confirmation = False

        self.trade_open = False

        self.retrace_time = None

        self.retrace_high = None

        self.retrace_low = None

        self.current_trade = None