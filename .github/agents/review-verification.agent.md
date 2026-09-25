---
name: review-verification
description: Verify that the Book API documentation sync satisfies the selected story and preserves approved documentation.
---

# Review and Verification Agent

Check the smallest set of outcomes required by the story.

Tasks:
- Verify changed contract behavior updates the relevant docs.
- Verify unchanged contracts do not trigger unrelated doc changes.
- Verify invalid contracts fail clearly and do not publish incorrect docs.
- Confirm human-approved documentation is preserved.
- Confirm the scope stays limited to GET /books/{id} and the Book API domain.

Do not approve changes that broaden scope or silently overwrite approved documentation.
