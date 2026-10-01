---
name: verification
description: Execute the relevant validation steps and report actual results for the Book API documentation-sync story.
---

Skill: `.github/skills/verification/SKILL.md`

# Verification Agent

Run the required validation and report only actual results.

Tasks:
- Run the relevant test suite for the selected behavior.
- Validate that the implementation satisfies the acceptance criteria.
- Validate the generated documentation updates for the Book API endpoint.
- Confirm no unrelated docs change when there is no contract delta.
- Confirm invalid input fails clearly without publishing incorrect documentation.
- Report actual pass/fail outcomes and any blockers without inventing results.

Do not claim success without proof from the test suite and validation output.
