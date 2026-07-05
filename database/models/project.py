from dataclasses import dataclass
from typing import Optional

from database.models.base_model import BaseModel


@dataclass
class Project(BaseModel):

    id: Optional[int] = None

    name: str = ""

    description: str = ""

    created_at: str = ""

    last_modified: str = ""

    @classmethod
    def from_row(cls, row):

        if row is None:
            return None

        data = dict(row)

        data["description"] = data.get("description") or ""
        data["created_at"] = data.get("created_at") or ""
        data["last_modified"] = data.get("last_modified") or ""

        return cls(**data)