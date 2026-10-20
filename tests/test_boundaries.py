from unittest.mock import Mock

import pytest
from errors import ValidationError
from gradebook import add_mark
from models import Mark

from rules import ensure_weight_fits


@pytest.mark.parametrize(
    ("weight", "should_pass"),
    [
        (0, True),
        (100, True),
        (100.01, False),
    ],
)
def test_weight_boundaries(weight, should_pass):
    if should_pass:
        ensure_weight_fits([], weight)
    else:
        with pytest.raises(ValidationError):
            ensure_weight_fits([], weight)


@pytest.mark.parametrize(
    ("score", "should_pass"),
    [
        (0, True),
        (20, True),
        (-0.01, False),
        (20.01, False),
    ],
)
def test_add_mark_score_boundaries(state, score, should_pass):
    save_mock = Mock()

    def fixed_now():
        return "2026-01-01T00:00:00"

    if should_pass:
        mark = Mark(student="2430-0129", assessment="A1", score=score)
        add_mark(state, mark, fixed_now, save_mock)
        assert any(m["score"] == score for m in state["marks"])
    else:
        initial_count = len(state["marks"])
        with pytest.raises(ValidationError):
            mark = Mark(student="2430-0129", assessment="A1", score=score)
            add_mark(state, mark, fixed_now, save_mock)
        assert len(state["marks"]) == initial_count
