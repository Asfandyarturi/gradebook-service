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
## Task 8 Final Summary
- Final overall coverage: 52%
- All tests passing: Yes (39 tests)
- Code quality checks: mypy --strict passed, ruff check passed
- Clean workspace verified.
## Lab 06 — Debugging and Regression Tests
| Bug | Cause | Fix | Test |
|---|---|---|---|
| A | To be investigated | Pending | Pending |
| B | To be investigated | Pending | Pending |
| C | To be investigated | Pending | Pending |
Task 3: Find Bug A with Git Bisect

First bad commit:
983a7f22b0dc62ecd66484b0e510839de8700c30

Commit message:
Task 2 step 3 update student id extraction

Rounds needed:
2

Cause:
The change from self.path.split("/")[2] to
self.path.removeprefix("/students/") caused trailing
slashes and query strings to become part of the student ID.
## Task 4: Fix Bug A

Added tests for:
- GET /students/S1
- GET /students/S1/
- GET /students/S1?format=json
- GET /students/NOPE/

Fix:
Updated student ID extraction in _get to remove query strings
and trailing slashes.

Test results:
27 passed.
## Task 5: Reproduce Bug B

Steps:
1. Created assessment A1 (weight 10, total 20).
2. Changed gradebook.json permissions to read-only using chmod 444.
3. Posted assessment A2 (weight 40, total 100).
4. Received HTTP 500 Internal Server Error.

Last traceback line:
PermissionError: [Errno 13] Permission denied: 'gradebook.json'

Code location:
gradebook.py, line 31:
with open(DATA, "w") as f:

After changing permissions back using chmod 644,
posted A2 again and received HTTP 409 Conflict:
assessment already exists.

Cause:
The assessment was added to memory before saving.
When saving failed, the assessment remained in memory.