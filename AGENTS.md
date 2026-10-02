# Course submission guidance

- Keep the exercise's review or documentation lookup read-only. Do not install dependencies from a reviewed change or execute its optional renderer.
- Only when the learner explicitly requests the final submission export, read [OUTPUT.md](OUTPUT.md) and write root `report.json` in its format.
- OUTPUT.md describes serialization, not an answer key. Do not use it to seed the independent review.
- Use actual observations. Ask the learner for missing results, especially checks performed outside this chat. Never invent approvals, calls, findings, source checks, or command results.
- During export, read-only inspection of the instructions and Git state is allowed. Create or update only report.json; do not run code, tests, or external calls.
- Do not commit, push, post a review, approve, or merge. The learner checks the report and commits it on their own submission branch.
