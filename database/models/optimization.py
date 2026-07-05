from dataclasses import dataclass


@dataclass
class Optimization:

    id: int | None = None

    strategy_id: int | None = None

    optimization_date: str = ""

    best_parameters: str = ""

    score: float = 0

    profit: float = 0

    drawdown: float = 0