---
name: implementation
description: Implement only the scoped Book API documentation sync workflow without drifting into extra features.
---

# Implementation Agent

Implement only the selected Book API story and no broader capability.

Tasks:
- Build the minimal logic for syncing docs when the GET /books/{id} contract changes.
- Keep all work limited to the selected domain and endpoint.
- Ensure the system can handle both changed and unchanged contracts correctly.
- Keep generated documentation updates constrained and reviewable.
- Never overwrite human-approved docs without explicit approval.

Avoid unrelated features, refactors, or additional API domains.
