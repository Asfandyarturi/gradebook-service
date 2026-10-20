from unittest.mock import Mock

import pytest
from errors import ConflictError, ValidationError
from gradebook import add_assessment


def test_add_valid_assessment(state):
    save_mock = Mock()
    assessment = {"id": "A3", "title": "Final", "weight": 50, "total": 100}

    add_assessment(state, assessment, save_mock)

    assert state["assessments"]["A3"] == assessment
    save_mock.assert_called_once()


def test_add_assessment_exceeds_weight(state):
    save_mock = Mock()
    assessment = {"id": "A3", "title": "Project", "weight": 70, "total": 100}

    with pytest.raises(ValidationError):
        add_assessment(state, assessment, save_mock)

    assert "A3" not in state.get("assessments", {})
    save_mock.assert_not_called()


def test_add_assessment_duplicate_id(state):
    save_mock = Mock()
    assessment = {"id": "A1", "title": "Duplicate Quiz", "weight": 10, "total": 20}

    with pytest.raises(ConflictError):
        add_assessment(state, assessment, save_mock)

    save_mock.assert_not_called()
