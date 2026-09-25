# Design Review Skill

## Purpose
Evaluate whether the proposed architecture satisfies the selected requirements and remains within scope.

## When to use
Use after architecture is drafted and before implementation begins.

## Responsibilities
- Trace architecture decisions to requirements and acceptance criteria.
- Identify design risks, gaps, assumptions, and unresolved decisions.
- Check the generated-documentation boundary and preservation of manual content.
- Check handling of valid, invalid, changed, and unchanged contracts.
- Record a clear review outcome and required corrections, if any.

## Inputs
- Approved requirements.
- Proposed architecture and data flow.
- Selected user story and acceptance criteria.

## Expected outputs
- Findings ordered by impact.
- Explicit decisions or required design corrections.
- A review status such as PASS or changes required.

## Constraints
- Review design only; do not implement code or change application source.
- Keep findings limited to the Book API GET /books/{id} documentation-sync scope.
- Do not replace the architecture with unrelated implementation detail.
- Treat human-approved documentation protection as a mandatory design concern.
