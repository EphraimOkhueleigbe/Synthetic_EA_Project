from dataclasses import dataclass
from typing import Optional

from database.models.base_model import BaseModel


@dataclass
class Backtest(BaseModel):

    id: Optional[int] = None

    project_id: Optional[int] = None

    strategy_id: Optional[int] = None

    symbol: str = ""

    start_date: str = ""

    end_date: str = ""

    status: str = "Pending"

    created_at: str = ""

    updated_at: str = ""

    @classmethod
    def from_row(cls, row):

        if row is None:
            return None

        return cls(**dict(row))