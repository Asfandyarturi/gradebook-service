from dataclasses import dataclass

from errors import ValidationError


@dataclass(frozen=True)
class Student:
    id: str
    name: str

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValidationError("id cannot be empty")
        if not self.name.strip():
            raise ValidationError("name cannot be empty")


@dataclass(frozen=True)
class Assessment:
    id: str
    title: str
    weight: float
    total: float

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValidationError("id cannot be empty")
        if not self.title.strip():
            raise ValidationError("title cannot be empty")
        if self.weight < 0 or self.weight > 100:
            raise ValidationError("weight must be between 0 and 100")
        if self.total <= 0:
            raise ValidationError("total must be greater than 0")


@dataclass(frozen=True)
class Mark:
    student: str
    assessment: str
    score: float

    def __post_init__(self) -> None:
        if self.score < 0:
            raise ValidationError("score cannot be negative")
