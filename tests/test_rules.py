import pytest
from errors import ValidationError
from rules import ensure_weight_fits


def test_empty_weights_fits():
    ensure_weight_fits([], 50)


def test_exceeds_max_weight_raises():
    with pytest.raises(ValidationError, match="100"):
        ensure_weight_fits([60], 50)


def test_exact_limit_fits():
    ensure_weight_fits([60], 40)
    
    
    
def test_float_precision_weights_fits():
    ensure_weight_fits([9.3, 27.3, 33.7], 29.7)
