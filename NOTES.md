Total coverage is 22%. The file with the lowest coverage is conftest.py.
Cycle 1: Fixed IndentationError and PYTHONPATH; test_empty_weights_fits passed.
Cycle 2 failure: Failed: DID NOT RAISE <class 'errors.ValidationError'>
Cycle 3 note: Did not fail first; passed immediately because 60 + 40 equals 100.
Cycle 4 failure: Total weight cannot exceed 100 due to float representation 100.00000000000001.
## Task 5 Coverage Analysis
- Final coverage total: 17%
- What coverage told us: Coverage identified which lines and decision branches executed during test runs.
- What coverage could not tell us: Coverage could not verify whether assertions were present or whether the output behavior was correct.
- Untested function in gradebook.py: load_state
## Task 6 Boundary Value Testing
- Mutation finding: Changing > to >= in add_mark caused test_add_mark_score_boundaries[20-True] to fail.
## Task 7 Property-Based Testing
- Properties verified: Valid sums (<= 100) never raise ValidationError; sums exceeding 100 + tolerance always raise ValidationError.
- Hypothesis value: Automatically generates edge cases (e.g., extremely tiny floating point decimals, zero weights) across hundreds of iterations.
