from dataclasses import asdict
import copy


class BaseModel:
    """
    Common functionality shared by all database models.
    """

    def to_dict(self):
        return asdict(self)

    def clone(self):
        return copy.deepcopy(self)