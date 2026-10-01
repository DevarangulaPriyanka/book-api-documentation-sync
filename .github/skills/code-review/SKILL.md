# Code Review Skill

## Purpose
Review the implementation for correctness, maintainability, safety, and alignment with the approved design.

## When to use
Use after implementation and focused tests are available, before final verification or PR preparation.

## Responsibilities
- Check behavior against requirements and acceptance criteria.
- Inspect validation, error handling, and no-op behavior.
- Confirm generated documentation updates are narrow and deterministic.
- Confirm human-maintained documentation is not overwritten.
- Check test coverage, dependency safety, clarity, and scope discipline.
- Report findings without claiming checks that were not performed.

## Inputs
- Implementation diff and relevant tests.
- Approved requirements, architecture, and implementation plan.
- Available test and validation results.

## Expected outputs
- Findings ordered by severity with concrete file or behavior references.
- Missing-test or residual-risk notes.
- A review status and concise summary after findings.

## Constraints
- Do not modify application source while reviewing.
- Review only the Book API GET /books/{id} documentation-sync change.
- Do not invent defects, validation results, or unrelated improvement work.
- Treat accidental overwrite of approved documentation as a high-priority defect.
