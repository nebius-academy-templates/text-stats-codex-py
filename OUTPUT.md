# Lesson 5 — final result format

Read this instruction only at the explicit final export, after the independent
review and learner verification. It is not a list of findings to search for.
Collect the learner's human-first questions only after the independent review.

Save root `report.json` using actual results supplied in the conversation. Ask
for missing observations. Read-only file and Git inspection is allowed during
export; do not execute code or tests, install dependencies, make external calls,
edit the application, commit, push, or post the review.

Use UTF-8 JSON, `schema_version: 1`, `lesson: 5`, and these exact keys. Free text
may use the learner's language. Do not include Markdown fences, duplicate keys,
placeholders, or an answer copied from this empty shape:

```json
{
  "schema_version": 1,
  "lesson": 5,
  "pr": {"url": "", "base": "", "head": "", "commit": "", "changed_files": []},
  "human_questions": [{"question": "", "observation": ""}],
  "model_findings": [{"id": "F1", "title": "", "location": {"path": "", "line": 1, "quote": ""}, "assessment": "", "reason": ""}],
  "missed_findings": [{"title": "", "evidence": ""}],
  "checks": {
    "baseline": {"command": "", "exit_code": 0, "output": ""},
    "normal": {"command": "", "exit_code": 0, "output": ""},
    "probes": [
      {"id": "representation", "command": "", "exit_code": 0, "output": "", "interpretation": ""},
      {"id": "file_boundary", "command": "", "exit_code": 0, "output": "", "interpretation": ""}
    ]
  },
  "risks": [{"class": "", "location": {"path": "", "line": 1, "quote": ""}, "execution_path": "", "evidence": "", "consequence": "", "mitigation": "", "certainty": ""}],
  "contributor_comment": "",
  "decision": "",
  "uncertainty": ""
}
```

## Field rules

- `pr`: the reviewed PR URL, branch names, full candidate commit SHA before your report commit, and complete changed-file list. Include the two supplied instruction files as well as the application change. Do not use your submission commit as the reviewed candidate.
- `human_questions`: at least one question and initial observation under each of the practice's four headings. These are the learner's manual pass, not reconstructed model findings.
- `model_findings`: one entry per actual finding, unique IDs, and assessment `Useful`, `Weak`, or `False`, with the learner's evidence-based reason. If there were no findings, use `[]`.
- `missed_findings`: only independently confirmed issues absent from that model run. Use `[]` when none were established. No finding is automatically a miss because a response was empty.
- Each `location` uses a repository-relative file path, one-based candidate line number, and a short exact code excerpt beginning on that line. Cite the reviewed code, not the submitted report.
- `checks.baseline`: the trusted-main test command and actual output before checking out the PR. `checks.normal`: the candidate suite using that same prepared virtual environment.
- `checks.probes`: both commands from the practice, with their actual exit codes, outputs, and interpretation. These commands print evidence; a successful process exit does not establish correct application behavior. Do not replace them with Go-style failing-test results.
- `risks`: one conclusion for each class examined: `correctness`, `resource_safety`, `dependency_api`, `provenance`. `certainty` is `confirmed` or `uncertain`. Explain the relevant path, evidence, consequence, and mitigation or evidence needed to resolve the uncertainty. For registry claims include the actual source, check date, and limitations in `evidence`. Do not infer infringement or package safety from absent evidence.
- `contributor_comment`: the learner-checked draft. Saving it does not post it to GitHub.
- `decision`: `ready`, `not-ready`, or `blocked-on-evidence`, matching the learner's conclusion. Record the result honestly; if required checks could not be completed, report the incomplete exercise rather than inventing passing checks.
- `uncertainty`: the remaining limitations, or an explicit statement that no further uncertainty was recorded.

Ask the learner to compare the report with the actual exercise and commit only
report.json on their own branch. The offline checker verifies structured evidence,
candidate citations, and unchanged fixture files. It cannot authenticate the
chat, external actions, or all free-text reasoning.
