# Documentation Sync Skill

## Purpose
Use this skill when the work involves syncing API contract changes to documentation while preserving human-approved content.

## Guardrails
- Keep the scope to the selected story and endpoint.
- Never overwrite manually approved documentation without explicit approval.
- Prefer narrow, generated updates over broad doc rewrites.
- Validate changed and unchanged contract cases before completion.

## Working style
- Start from the source contract.
- Update only the relevant doc sections.
- Confirm the changes are minimal, reviewable, and traceable to the selected endpoint.
