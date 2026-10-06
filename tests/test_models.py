import pytest

from errors import ValidationError
from models import parse_assessment, parse_mark


def test_numeric_string_accepted():
    mark = parse_mark({"student": "S1", "assessment": "A1", "score": "50"})
    assert mark.score == 50.0


def test_text_rejected():
    with pytest.raises(ValidationError):
        parse_mark({"student": "S1", "assessment": "A1", "score": "abc"})


def test_bool_rejected():
    with pytest.raises(ValidationError):
        parse_mark({"student": "S1", "assessment": "A1", "score": True})


def test_nan_rejected():
    with pytest.raises(ValidationError):
        parse_mark({"student": "S1", "assessment": "A1", "score": "nan"})


def test_zero_total_rejected():
    with pytest.raises(ValidationError):
        parse_assessment(
            {"id": "A1", "title": "Quiz", "weight": 20, "total": 0}
        )


def test_negative_score_rejected():
    with pytest.raises(ValidationError):
        parse_mark({"student": "S1", "assessment": "A1", "score": -5})


def test_missing_field_rejected():
    with pytest.raises(ValidationError):
        parse_mark({"student": "S1", "assessment": "A1"})


def test_payload_not_dict_rejected():
    with pytest.raises(ValidationError):
        parse_mark("not a dict")


def test_valid_assessment():
    assessment = parse_assessment(
        {"id": "A1", "title": "Quiz", "weight": "20", "total": "100"}
    )
    assert assessment.id == "A1"
    assert assessment.title == "Quiz"
    assert assessment.weight == 20.0
    assert assessment.total == 100.0
