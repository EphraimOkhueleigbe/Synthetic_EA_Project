from dataclasses import dataclass
from typing import Optional

from database.models.base_model import BaseModel


@dataclass
class Project(BaseModel):

    id: Optional[int] = None

    name: str = ""

    description: str = ""

    created_at: str = ""

    updated_at: str = ""

    @classmethod
    def from_row(cls, row):

        if row is None:
            return None

        data = dict(row)

        data["description"] = data.get("description") or ""

        data["created_at"] = data.get("created_at") or ""

        data["updated_at"] = data.get("updated_at") or ""

        return cls(**data)