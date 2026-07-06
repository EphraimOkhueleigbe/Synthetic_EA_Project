from dataclasses import dataclass


@dataclass
class Backtest:

    id: int | None = None

    strategy_id: int | None = None

    test_date: str = ""

    symbol: str = ""

    timeframe: str = ""

    starting_balance: float = 0

    ending_balance: float = 0

    net_profit: float = 0

    win_rate: float = 0

    profit_factor: float = 0

    max_drawdown: float = 0