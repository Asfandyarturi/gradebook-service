(e) Deleted gradebook.json again, restarted the service, then tried to add a mark for a non-existing assessment.

Command:
curl -i -X POST localhost:8000/marks -d '{"student":"S1","assessment":"NOPE","score":"10"}'

Result:
HTTP/1.0 200 OK
{"error": "no such student"}

The service returned 200 OK instead of an appropriate error status.(e) Deleted gradebook.json again, restarted the service, then tried to add a mark for a non-existing assessment.

Command:
curl -i -X POST localhost:8000/marks -d '{"student":"S1","assessment":"NOPE","score":"10"}'

Result:
HTTP/1.0 200 OK
{"error": "no such student"}

The service returned 200 OK instead of an appropriate error status.(d) Deleted gradebook.json, restarted the service, created S1, created A1 with total 0, added a mark, then requested /report.

Result:
POST /students -> 200 OK
POST /assessments -> 200 OK
POST /marks -> 200 OK
GET /report -> curl: (52) Empty reply from server

The service fails while generating the report when total is 0.(d) Deleted gradebook.json, restarted the service, created S1, created A1 with total 0, added a mark, then requested /report.

Result:
POST /students -> 200 OK
POST /assessments -> 200 OK
POST /marks -> 200 OK
GET /report -> curl: (52) Empty reply from server

The service fails while generating the report when total is 0.

Task 2(c)

Create student:
curl -i -X POST localhost:8000/students -d '{"id":"S1","name":"Ayesha"}'(d) Deleted gradebook.json, restarted the service, created S1, created A1 with total 0, added a mark, then requested /report.

Result:
POST /students -> 200 OK
POST /assessments -> 200 OK
POST /marks -> 200 OK
GET /report -> curl: (52) Empty reply from server

The service fails while generating the report when total is 0.Task 2(c)

Create student:
curl -i -X POST localhost:8000/students -d '{"id":"S1","name":"Ayesha"}'
Result:
HTTP 200 OK
{"error": "exists"}

Create assessment:
curl -i -X POST localhost:8000/assessments -d '{"id":"A1","title":"Math","weight":"100","total":"100"}'
Result:
HTTP 200 OK
{"id": "A1", "title": "Math", "weight": "100", "total": "100"}

Post invalid mark:
curl -i -X POST localhost:8000/marks -d '{"student":"S1","assessment":"A1","score":"abc"}'
Result:
HTTP 200 OK
{"ok": true}

Get student:
curl -i localhost:8000/students/S1
Result:
curl: (52) Empty reply from serverTask 2(b)
Command:
curl -i -X POST localhost:8000/students -d '5'

Result:
curl: (52) Empty reply from serverTask 2(b)
Command:
curl -i -X POST localhost:8000/students -d '5'

Result:
[write the HTTP response you get here]Task 2(a)
Command:
curl -i localhost:8000/students/NOPE

Result:
HTTP 200 OK with {"error": "not found"}

Expected:
404 Not Found
Ruff check:

Command:
ruff check .

Result:
Found 10 errors.
2 errors are fixable with the --fix option.
Bare except statements:

Line 19
Line 28
Line 84
