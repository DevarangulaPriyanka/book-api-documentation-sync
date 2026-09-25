# Architecture Skill

## Purpose
Define the minimum architecture for synchronizing documentation from the selected Book API contract.

## When to use
Use after requirements are agreed and before implementation planning or coding begins.

## Responsibilities
- Identify the source of truth for the GET /books/{id} contract.
- Define the contract-change detection and synchronization flow.
- Define the boundary between generated and human-maintained documentation.
- Describe validation and failure handling at the architectural level.
- Keep components and data flow minimal and explicit.

## Inputs
- Approved requirements and acceptance criteria.
- The selected user story and scope boundaries.
- Existing repository structure and constraints.

## Expected outputs
- A minimal architecture and data-flow description.
- Clear ownership of contract validation, change detection, rendering, and documentation updates.
- Decisions that trace back to the requirements.

## Constraints
- Design only the Book API GET /books/{id} workflow.
- Do not introduce platform-wide abstractions, extra services, or unrelated endpoints.
- Do not implement application code or prescribe detailed test cases.
- Ensure human-approved documentation remains protected.
