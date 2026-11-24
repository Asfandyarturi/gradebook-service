import pytest

from gradebook import add_assessment


def test_failed_save_leaves_no_trace(loaded):
    assessment = {
        "id": "A3",
        "title": "Final",
        "weight": 10.0,
        "total": 50.0,
    }

    def fail_save():
        raise OSError("disk full")

    with pytest.raises(OSError):
        add_assessment(loaded, assessment, fail_save)

    assert "A3" not in loaded["assessments"]
