from app.engine.statistics import StatisticsEngine
from app.engine.signals import SignalGenerator
from app.engine.ema import EMA
from app.engine.simulator import Trade
from app.engine.simulator import TradeSimulator


class Backtester:

    def __init__(self):

        self.trades = []

        self.statistics = None

    # =====================================================

    def clear(self):

        self.trades.clear()

        self.statistics = None

    # =====================================================

    def run(

        self,

        candles,

        fast_period=9,

        slow_period=18

    ):

        self.clear()

        closes = [

            candle.close

            for candle in candles

        ]

        fast = EMA.calculate(

            closes,

            fast_period

        )

        slow = EMA.calculate(

            closes,

            slow_period

        )

        start = slow_period

        for i in range(start, len(closes)):

            signal = SignalGenerator.ema_crossover(

                fast[i - 1],
                slow[i - 1],

                fast[i],
                slow[i]

            )

            if signal is None:

                continue

            entry = closes[i]

            # -------------------------------------
            # Temporary SL / TP
            # (Only for testing)
            # -------------------------------------

            if signal == TradeSimulator.BUY:

                stop_loss = entry - 5

                take_profit = entry + 5

            else:

                stop_loss = entry + 5

                take_profit = entry - 5

            trade = Trade(

                direction=signal,

                entry=entry,

                stop_loss=stop_loss,

                take_profit=take_profit,

                lot_size=1,

                open_time=candles[i].time

            )

            remaining_candles = candles[i + 1:]

            TradeSimulator.simulate(

                trade,

                remaining_candles

            )

            self.trades.append(trade)

        self.statistics = StatisticsEngine.calculate(

            self.trades

        )

        return self.statistics