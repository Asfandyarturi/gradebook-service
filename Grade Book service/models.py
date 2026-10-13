import math
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
def parse_number(raw: object, field: str) -> float:
    if isinstance(raw, bool):
        raise ValidationError(f"{field} must be a number")

    if isinstance(raw, (int, float)):
        value = float(raw)
    elif isinstance(raw, str):
        try:
            value = float(raw)
        except ValueError:
            raise ValidationError(f"{field} must be a number")
    else:
        raise ValidationError(f"{field} must be a number")

    if not math.isfinite(value):
        raise ValidationError(f"{field} must be finite")

    return value
def parse_text(raw: object, field: str) -> str:
    if not isinstance(raw, str) or not raw.strip():
        raise ValidationError(f"{field} must be a non-empty string")
    return raw.strip()
def parse_student(raw: object) -> Student:
    if not isinstance(raw, dict):
        raise ValidationError("student must be an object")

    if "id" not in raw:
        raise ValidationError("id is required")

    if "name" not in raw:
        raise ValidationError("name is required")

    student_id = parse_text(raw["id"], "id")
    name = parse_text(raw["name"], "name")

    return Student(student_id, name)
def parse_assessment(raw: object) -> Assessment:
    if not isinstance(raw, dict):
        raise ValidationError("assessment must be an object")

    if "id" not in raw:
        raise ValidationError("id is required")

    if "title" not in raw:
        raise ValidationError("title is required")

    if "weight" not in raw:
        raise ValidationError("weight is required")

    if "total" not in raw:
        raise ValidationError("total is required")

    assessment_id = parse_text(raw["id"], "id")
    title = parse_text(raw["title"], "title")
    weight = parse_number(raw["weight"], "weight")
    total = parse_number(raw["total"], "total")

    return Assessment(assessment_id, title, weight, total)
def parse_mark(raw: object) -> Mark:
    if not isinstance(raw, dict):
        raise ValidationError("mark must be an object")

    if "student" not in raw:
        raise ValidationError("student is required")

    if "assessment" not in raw:
        raise ValidationError("assessment is required")

    if "score" not in raw:
        raise ValidationError("score is required")

    student = parse_text(raw["student"], "student")
    assessment = parse_text(raw["assessment"], "assessment")
    score = parse_number(raw["score"], "score")

    return Mark(student, assessment, score)
