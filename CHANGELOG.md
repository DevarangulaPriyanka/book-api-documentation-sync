# Changelog

## Unreleased

### Added
- Added the Book API documentation sync workflow for GET /books/{id}.
- Implemented contract-change detection so the generated endpoint documentation updates only when the endpoint contract changes.
- Added deterministic documentation synchronization with a limited generated section for the selected endpoint.
- Added validation and error handling so invalid contract input fails clearly without publishing incorrect documentation.
- Added automated tests covering valid updates, unchanged-contract no-op behavior, invalid contract rejection, and preservation of manually maintained documentation outside the generated section.
- Verified the selected story with the available unittest suite and recorded the actual results.

### Orchestration

- Added an SDLC orchestrator agent to coordinate the documented development stages.
- Added sequential artifact-based handoffs between SDLC stages.
- Added stage validation and approval gates before proceeding to dependent stages.
- Added failure handling that stops orchestration when a stage does not complete successfully.
- The orchestrator does not automatically commit, push, or create a pull request.