from dataclasses import dataclass


@dataclass
class Statistics:

    total_trades: int = 0

    winners: int = 0

    losers: int = 0

    win_rate: float = 0.0

    total_profit: float = 0.0

    average_profit: float = 0.0

    average_loss: float = 0.0

    profit_factor: float = 0.0

    expectancy: float = 0.0

    max_drawdown: float = 0.0


class StatisticsEngine:

    @staticmethod
    def calculate(trades):

        stats = Statistics()

        stats.total_trades = len(trades)

        if stats.total_trades == 0:
            return stats

        winners = [
            t for t in trades
            if t.profit > 0
        ]

        losers = [
            t for t in trades
            if t.profit <= 0
        ]

        stats.winners = len(winners)

        stats.losers = len(losers)

        stats.win_rate = (
            stats.winners /
            stats.total_trades
        ) * 100

        stats.total_profit = sum(
            t.profit for t in trades
        )

        if winners:

            stats.average_profit = (

                sum(t.profit for t in winners)

                / len(winners)

            )

        if losers:

            stats.average_loss = (

                sum(abs(t.profit) for t in losers)

                / len(losers)

            )

        gross_profit = sum(
            t.profit
            for t in winners
        )

        gross_loss = sum(
            abs(t.profit)
            for t in losers
        )

        if gross_loss > 0:

            stats.profit_factor = (
                gross_profit /
                gross_loss
            )

        if stats.total_trades > 0:

            stats.expectancy = (
                stats.total_profit /
                stats.total_trades
            )

        # -----------------------------
        # Drawdown
        # -----------------------------

        equity = 0

        peak = 0

        max_dd = 0

        for trade in trades:

            equity += trade.profit

            if equity > peak:
                peak = equity

            dd = peak - equity

            if dd > max_dd:
                max_dd = dd

        stats.max_drawdown = max_dd

        return stats