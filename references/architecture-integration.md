# Lighthouse and the Federated Work Graph

Lighthouse Keeper is a read-and-synthesize projection over the Navy Yard Work
Graph. It does not become a new database, a routing plane, or a general
communications department.

## System authorities

| Layer | Canonical system | Lighthouse relationship |
|---|---|---|
| Organizational commitment | Linear | Read authorized commitments and meaningful updates; attach packet-linked review or follow-up references only when authorized. |
| Agent execution | Beads | Read bounded summaries, dependencies, blockers, handoffs, and discoveries; never treat activity as institutional progress. |
| Institutional memory | Notion | Store the canonical Signal Packet and packet-linked learning, correction, and publication records when authorized. |
| Implementation memory | GitHub | Link versioned code, skills, releases, and documentation as evidence. |
| Control plane | Hermes | Request identity, context, reconciliation, approval, or follow-up operations tied to a packet; do not route work or allocate resources. |
| Navigation projection | Navy Yard Chart | Read relevant projections; do not create a competing chart or source of truth. |

## Packet identity

Every material packet should preserve applicable stable references:

```yaml
signal_id: lighthouse-YYYYMMDD-###
linear_issue_ids: []
bead_ids: []
notion_page_ids: []
github_refs: []
evaluation_run_ids: []
capability_harvest_ids: []
hermes_run_id: null
```

Use identifiers and links rather than copying whole source records. When
fields disagree, preserve both observations, identify the relevant authority,
and request reconciliation.

## Packet-first boundary

The communication path is:

`source record -> Signal Packet -> bounded audience projection -> approval -> reception/correction -> learning link`

Lighthouse Keeper does not run an announcement calendar, campaign, newsletter
pipeline, cross-project queue, worker assignment, capacity reservation, or
execution dispatch. A packet-linked request to another system is a handoff,
not a transfer of authority.

## Capability harvest

At meaningful closeout, the packet may link to a capability harvest that
separately records artifact outcome and capability outcome. The owning role
remains responsible for the capability record; Lighthouse Keeper only makes
the warranted signal legible.
