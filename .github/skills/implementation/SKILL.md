# Implementation Skill

## Purpose
Implement the smallest working Book API documentation-sync workflow described by the approved requirements and architecture.

## When to use
Use after requirements, architecture, and design review are complete and implementation work is authorized.

## Responsibilities
- Implement contract representation and validation for GET /books/{id}.
- Detect contract changes and no-op cases deterministically.
- Render and update only the generated documentation section.
- Preserve manually maintained documentation outside the generated section.
- Add focused tests for the approved behavior.

## Inputs
- Approved requirements and acceptance criteria.
- Reviewed architecture and implementation plan.
- Existing repository conventions and test setup.

## Expected outputs
- Minimal application changes implementing the approved workflow.
- Focused automated tests for changed, unchanged, valid, and invalid contract cases.
- A result that is ready for code review without unrelated scope changes.

## Constraints
- Modify only the scoped Book API documentation-sync implementation and its tests when authorized.
- Do not add unrelated APIs, endpoints, features, dependencies, or refactors.
- Never overwrite human-approved documentation without explicit approval.
- Keep generated output deterministic and failures clear.
