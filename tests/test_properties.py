import pytest
from hypothesis import given, strategies as st
from errors import ValidationError
from rules import MAX_TOTAL_WEIGHT, TOLERANCE, ensure_weight_fits


# Property 1: Valid sums (<= 100) must never raise ValidationError
@given(
    weights=st.lists(
        st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
        max_size=10,
    ),
    new_weight=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
)
def test_valid_weights_property(weights, new_weight):
    total = sum(weights) + new_weight
    if total <= MAX_TOTAL_WEIGHT:
        ensure_weight_fits(weights, new_weight)


# Property 2: Exceeding sums (> 100 + TOLERANCE) must always raise ValidationError
@given(
    weights=st.lists(
        st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
        min_size=1,
        max_size=10,
    ),
    new_weight=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
)
def test_exceeding_weights_property(weights, new_weight):
    total = sum(weights) + new_weight
    if total > MAX_TOTAL_WEIGHT + TOLERANCE:
        with pytest.raises(ValidationError):
            ensure_weight_fits(weights, new_weight)
