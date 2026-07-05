from dataclasses import dataclass
from typing import Optional

from database.models.base_model import BaseModel


@dataclass
class Strategy(BaseModel):

    id: Optional[int] = None

    project_id: Optional[int] = None

    name: str = ""

    d1_fast_ema: int = 9
    d1_slow_ema: int = 18

    m30_fast_ema: int = 9
    m30_slow_ema: int = 18

    risk_formula: str = ""

    stop_loss_type: str = ""
    stop_loss_value: float = 0.0

    take_profit_type: str = ""
    take_profit_value: float = 0.0

    trade_direction: str = "Trend"

    active: int = 1

    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def from_row(cls, row):

        if row is None:
            return None

        data = dict(row)

        for key, value in data.items():
            if value is None:
                if isinstance(getattr(cls, key, ""), str):
                    data[key] = ""

        return cls(**data)