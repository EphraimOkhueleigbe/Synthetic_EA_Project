from dataclasses import dataclass


@dataclass
class Trade:

    direction: str

    entry: float

    stop_loss: float

    take_profit: float

    lot_size: float

    open_time: object = None

    close_time: object = None

    exit_price: float = 0.0

    result: str = ""

    profit: float = 0.0

    closed: bool = False


class TradeSimulator:
    """
    Simulates a trade candle-by-candle until
    either the Stop Loss or Take Profit is hit.
    """

    BUY = "BUY"
    SELL = "SELL"

    WIN = "WIN"
    LOSS = "LOSS"

    @staticmethod
    def simulate(trade, candles):

        for candle in candles:

            # ==========================
            # BUY TRADE
            # ==========================

            if trade.direction == TradeSimulator.BUY:

                # Stop Loss hit

                if candle.low <= trade.stop_loss:

                    trade.closed = True
                    trade.result = TradeSimulator.LOSS
                    trade.exit_price = trade.stop_loss
                    trade.close_time = candle.time

                    trade.profit = (
                        trade.stop_loss - trade.entry
                    ) * trade.lot_size

                    return trade

                # Take Profit hit

                elif candle.high >= trade.take_profit:

                    trade.closed = True
                    trade.result = TradeSimulator.WIN
                    trade.exit_price = trade.take_profit
                    trade.close_time = candle.time

                    trade.profit = (
                        trade.take_profit - trade.entry
                    ) * trade.lot_size

                    return trade

            # ==========================
            # SELL TRADE
            # ==========================

            elif trade.direction == TradeSimulator.SELL:

                # Stop Loss hit

                if candle.high >= trade.stop_loss:

                    trade.closed = True
                    trade.result = TradeSimulator.LOSS
                    trade.exit_price = trade.stop_loss
                    trade.close_time = candle.time

                    trade.profit = (
                        trade.entry - trade.stop_loss
                    ) * trade.lot_size

                    return trade

                # Take Profit hit

                elif candle.low <= trade.take_profit:

                    trade.closed = True
                    trade.result = TradeSimulator.WIN
                    trade.exit_price = trade.take_profit
                    trade.close_time = candle.time

                    trade.profit = (
                        trade.entry - trade.take_profit
                    ) * trade.lot_size

                    return trade

        return trade