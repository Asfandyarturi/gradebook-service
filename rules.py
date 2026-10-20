from errors import ValidationError  # type: ignore[import-untyped]

MAX_TOTAL_WEIGHT: float = 100.0
TOLERANCE: float = 1e-9


def ensure_weight_fits(existing_weights: list[float], new_weight: float) -> None:
    """Ensure total assessment weight does not exceed the allowed maximum."""
    if sum(existing_weights) + new_weight > MAX_TOTAL_WEIGHT + TOLERANCE:
        raise ValidationError("Total weight cannot exceed 100")
