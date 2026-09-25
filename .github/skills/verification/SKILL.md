# Verification Skill

## Purpose
Verify the completed Book API documentation-sync workflow using executable checks and report actual evidence.

## When to use
Use after implementation and code review, before final validation and pull-request preparation.

## Responsibilities
- Run the relevant automated test suite.
- Exercise the changed-contract and unchanged-contract cases.
- Verify valid contracts synchronize successfully.
- Verify invalid contracts fail clearly without publishing incorrect documentation.
- Confirm manually maintained documentation is preserved.
- Report exact pass, fail, warning, and blocker results.

## Inputs
- Implemented code and tests.
- Acceptance criteria and validation commands.
- Documentation artifacts and any documented limitations.

## Expected outputs
- Reproducible commands and their actual results.
- Acceptance-criteria pass or fail evidence.
- Clearly separated warnings, limitations, and blockers.

## Constraints
- Do not claim success without executable evidence.
- Do not modify application source, tests, or approved capstone artifacts while verifying.
- Keep verification limited to the Book API GET /books/{id} documentation-sync scope.
- Report documented warnings accurately; do not present warning-bearing validation as clean.
