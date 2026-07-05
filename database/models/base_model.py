from dataclasses import asdict


class BaseModel:

    def to_dict(self):
        return asdict(self)

    def copy(self):
        return self.__class__(**self.to_dict())