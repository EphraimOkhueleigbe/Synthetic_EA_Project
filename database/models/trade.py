from dataclasses import dataclass


@dataclass
class Trade:

    id: int | None = None

    backtest_id: int | None = None

    direction: str = ""

    entry_price: float = 0

    exit_price: float = 0

    stop_loss: float = 0

    take_profit: float = 0

    profit: float = 0

    result: str = ""

    entry_time: str = ""

    exit_time: str = ""