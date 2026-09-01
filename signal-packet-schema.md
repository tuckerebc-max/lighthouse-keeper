# Signal Packet Schema v1

`SignalPacket` is the canonical internal object that precedes any material
communication projection. The JSON Schema in
`schemas/signal-packet.schema.json` is authoritative for machine validation.

```yaml
schema_version: lighthouse-keeper.signal-packet.v1
signal_id: lighthouse-YYYYMMDD-###
title: "Short descriptive title"
signal_type: milestone | capability_gain | learning | decision | failure_repair | direction | boundary | invitation | correction | no_material_signal
scope:
  institution: navy_yard
  project: null
  client: null
  workbench: null
  audience_scope: []
source_window:
  start: YYYY-MM-DD
  end: YYYY-MM-DD
source_refs:
  linear_issue_ids: []
  bead_ids: []
  notion_page_ids: []
  github_refs: []
  evaluation_run_ids: []
  capability_harvest_ids: []
  hermes_run_id: null
observation: "What the records directly show."
reconstruction: "What sequence or context produced the observation."
claim: "What can responsibly be said."
evidence:
  - ref: "stable source identifier"
    supports: "What this source supports."
warrant: "Why the evidence supports the claim in this context."
counterclaim: null
uncertainties: []
boundaries: ["What the packet does not authorize or establish."]
sensitivity: public | leadership | internal | restricted | client_restricted
confidence: low | medium | high | unknown
freshness_as_of: YYYY-MM-DD
what_changed: "The meaningful change."
why_it_matters: "The institutional or audience significance."
what_follows: "Decision, test, build, maintenance action, or invitation."
maturity: candidate | source_assembled | analyzed | drafted | boundary_checked | approved | published | monitored | corrected | superseded | retired
audiences: [internal_operators]
approval:
  required: true
  state: pending
```

Minimum completeness requires a bounded window, stable source reference, a
specific claim or explicit no-signal determination, evidence, warrant,
uncertainty or counterclaim where relevant, sensitivity, audience, significance,
next move, and approval state. Packet-linked audience prose cannot substitute
for these fields.
