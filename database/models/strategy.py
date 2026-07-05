from dataclasses import dataclass
from datetime import datetime


@dataclass
class Strategy:

    id: int | None = None

    project_id: int | None = None

    name: str = ""

    ema_fast: int = 9

    ema_slow: int = 18

    risk_formula: str = ""

    take_profit: float = 0

    created_at: datetime | None = None