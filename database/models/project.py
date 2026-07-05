from dataclasses import dataclass
from datetime import datetime

from database.models.base_model import BaseModel


@dataclass
class Project(BaseModel):

    id: int | None = None

    name: str = ""

    description: str = ""

    created_at: datetime | None = None

    last_modified: datetime | None = None

    @classmethod
    def from_row(cls, row):

        return cls(**dict(row))