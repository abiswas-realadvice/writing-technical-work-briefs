---
type: regex
target:
  source: file
  path: design-check.txt
pattern: 'RESULT: PASS|"result": "PASS"'
match: contains
---
