---
description: Asks for a one-page brief from a dense technical excerpt; checks the skill fires, an HTML brief is produced, the bundled design checker is actually run, and it reports PASS. Needs `--allow-tools Write Bash` on the command line (allowed_tools here only grants the read-only subset).
tags: [smoke, design]
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Skill]
---

We have a dense internal writeup about our risk-scoring model that needs to become a one-page executive brief before Thursday's Risk Committee meeting.

Context: three model generations exist. The current one (M3.2) maps controls to 205 risk scenarios (189 are covered). A 500-deal simulation shows modeled unresolved-release exposure falling from 84% in the baseline configuration to 10% once a proposed release gate is added, assuming the gate operates at 84% effectiveness (not yet measured in production). Sixteen scenarios have no software control at all and need named owners before go-live.

Turn this into a one-page executive brief. Save it as a self-contained HTML file at `output.html`. Then run the bundled design checker against it and save its output to `design-check.txt`.
