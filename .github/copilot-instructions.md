# Copilot Project Instructions

## Project purpose
This project demonstrates the Automated Documentation Sync use case for the Book API. The goal is to keep API documentation aligned with the source contract while protecting human-approved documentation from accidental overwrite.

## Selected user story
As a backend developer working on the Book API, I want the API documentation for a single endpoint to sync automatically when the contract changes, so the published docs stay accurate without manual updates.

## Scope boundaries
- In scope: the Book API only.
- In scope: a single endpoint, GET /books/{id}.
- In scope: a minimal contract-to-documentation sync workflow.
- Out of scope: other APIs, other endpoints, UI work, unrelated docs, authentication, billing, versioning, localization, and broad platform automation.
- Keep the solution small and testable within this capstone.

## Human-approved documentation protection
- Preserve any human-approved or manually curated documentation content.
- Do not overwrite approved documentation sections without explicit human approval.
- Treat generated documentation as a constrained, reviewable artifact, not a place for unchecked edits.

## Testing expectations
- Validate the smallest behavior needed for the selected story.
- Confirm that documentation updates occur only when the contract changes.
- Confirm no unrelated docs change when there is no contract delta.
- Confirm invalid input fails clearly without publishing incorrect documentation.

## Git and PR expectations
- Keep each change small, reviewable, and tied to the selected story.
- Do not create a PR before review and validation are complete.
- Use commit messages and PR summaries that clearly explain the Book API documentation sync change and any validation performed.
