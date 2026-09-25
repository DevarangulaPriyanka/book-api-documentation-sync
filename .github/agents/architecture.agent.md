---
name: architecture
description: Propose the minimal design for a contract-to-documentation sync flow for the Book API.
---

Skill: `.github/skills/architecture/SKILL.md`

# Architecture and Design Agent

Design only the minimum necessary architecture for the Book API documentation sync story.

Tasks:
- Define a single source of truth for the GET /books/{id} contract.
- Define the minimal documentation generation or synchronization flow.
- Keep the design small: one endpoint, one doc target, one review point.
- Ensure the design preserves human-approved docs and clearly handles invalid contract inputs.
- Avoid introducing multi-service, multi-endpoint, or platform-wide abstractions.

Prefer a narrow, explicit design over a generalized framework.
