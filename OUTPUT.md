# Lesson 7 — final result format

Read this file only at the final export, after the bounded documentation lookup
and learner verification, or after recording why the task could not be completed.
This is a formatting instruction, not an answer to the Git question.

When explicitly asked, create root `report.json` from actual observations.
Reading this instruction and inspecting Git state is allowed during export.
Do not repeat the lookup, execute Git examples, run tests or application code,
change MCP configuration, modify other files, commit, or push.
Ask for the learner's policy decision and independent source-check observations;
a tool response does not establish that the learner opened its source.

Use UTF-8 JSON with the exact keys below, `schema_version: 1`, and `lesson: 7`.
Free text may use the learner's language. Machine keys and choices stay fixed.
Do not submit empty examples, duplicate keys, placeholders, or Markdown fences.

```json
{
  "schema_version": 1,
  "lesson": 7,
  "outcome": "",
  "why_external": "",
  "policy": {"decision": "", "basis": ""},
  "provider": "Context7",
  "library": "/git/htmldocs",
  "activity": {"external_calls": 0, "repository_commands": 0, "file_changes": 0, "other_activity": ""},
  "tool": null,
  "model_conclusion": null,
  "verification": null,
  "unavailable": null,
  "boundary_failure": null,
  "reusable_rule": ""
}
```

## Common fields

- `outcome`: `verified`, `unavailable`, or `boundary-failure`.
- `why_external`: why this repository cannot establish the current documentation answer.
- `policy.decision`: `approved`, `not-approved`, or `unknown`. `basis`: actual applicable policy evidence, not merely a Connected badge.
- `provider` and `library`: the intended boundary shown above, not invented evidence of actual usage.
- `activity`: observed counts during the lookup phase, excluding the later export and learner submission commands. Use `other_activity` to describe what happened, including an explicit absence of other activity when applicable.
- `tool`, if a call occurred: `{"name":"", "query":"", "library":"", "excerpt":"", "source_url":null}`. Record the actual call; do not rewrite an out-of-scope call as compliant. The source URL is null if none was returned. Use null for the whole tool object if no call occurred.
- `model_conclusion`: the actual answer, including errors; null if no substantive answer was returned.
- `reusable_rule`: what you would check before accepting another MCP-backed answer.

## Verified result

Set `outcome: "verified"` only after the permitted lookup and independent source
check. Set `unavailable` and `boundary_failure` to null. Supply:

```json
{
  "verification": {
    "source_url": "",
    "source_observation": "",
    "verdict": "",
    "normal_removal": "",
    "unclean_removal": "",
    "submodule_removal": "",
    "locked_removal": "",
    "learner_confirmed": true
  }
}
```

- `source_url`: the official Git git-worktree documentation page independently opened by the learner. `source_observation`: relevant section or short paraphrase mapping claims to source evidence.
- `verdict`: `supported` or `contradicted`, comparing the actual model answer to the source. A wrong model answer can still be correctly verified and rejected.
- `normal_removal`: `clean-unlocked-no-submodules` or `any-linked-worktree`.
- `unclean_removal` and `submodule_removal`: `requires-force`, `allowed-without-force`, or `never-allowed`.
- `locked_removal`: `requires-force-twice`, `requires-force-once`, or `never-allowed`.
- These choices record the learner's source-checked conclusions, not unchecked model claims. `learner_confirmed` is true only after the learner supplies that check; otherwise ask.

## Unavailable result

Set `outcome: "unavailable"`, `verification: null`, `boundary_failure: null`.
Keep actual partial tool/answer evidence or null when not attempted. Supply:

```json
{"unavailable": {"step":"", "observation":"", "checked":"", "gap":"", "next_step":""}}
```

`step`: `policy`, `connection`, `library`, `tool-call`, `source`, or `verification`.
State what was observed, what was actually checked, the remaining evidence gap,
and a safe next step. If policy is unknown or not approved, stop without a call.

## Boundary failure

Set `outcome: "boundary-failure"`, `verification: null`, `unavailable: null`.
Preserve the actual activity and any tool/answer evidence. Supply:

```json
{"boundary_failure": {"rule":"", "observation":"", "stopped":true, "gap":"", "next_step":""}}
```

`rule`: `provider`, `library`, `call-count`, `repository-action`,
`missing-source`, or `memory-substitution`. Describe the evidence and the safe
stop. Do not rerun to replace the observed failure with a preferable result.
Recording a failure does not authorize keeping application changes: only the
report is submitted. Do not discard unfamiliar work to satisfy a checker.

Ask the learner to verify and commit only report.json. The checker validates
the artifact, source boundary, outcome consistency, and intact fixture files;
it does not authenticate tool history or perform source checks for the learner.
