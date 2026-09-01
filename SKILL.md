---
name: lighthouse-keeper
description: Compile warranted Navy Yard Signal Packets from evidence-bearing Work Graph changes and attach bounded audience projections; use for signal triage, packet construction, correction, and capability-harvest linkage, not general communications, routing, or source-system mutation.
---

# Lighthouse Keeper Skill

Compile meaningful, evidence-bearing changes in the Navy Yard Work Graph into
`SignalPacket` records. A packet is the primary output; an audience brief,
report, or public draft is only a bounded projection attached to that packet.
This skill owns signal synthesis and packet integrity, not general
communications, routing, execution, canonical state, evaluation authority, or
publication by default.

The package is version `0.1.0` and remains a candidate. The role contract is
`navy-yard.lighthouse-keeper` at the source-aligned draft version recorded in
`manifest.json`.

## When to use

Use when a bounded reporting window may contain a meaningful capability gain,
decision, learning, failure/repair, boundary, direction, invitation,
correction, or explicit no-material-signal result. Do not convert every issue,
Bead, commit, heartbeat, or conversation into a signal.

Do not use this skill for a general announcement calendar, campaign,
newsletter pipeline, cross-project triage, workbench selection, capacity
allocation, worker assignment, specialist execution, or repair of a canonical
source record. Hand those requests to the responsible communication,
control-plane, workbench, or owning-record function.

## Procedure

1. Define the institution, project scope, reporting window, sensitivity,
   audience, and purpose. Record the packet identifier before drafting.
2. Assemble only authorized source records from the relevant systems. Preserve
   stable identifiers, source authority, observation time, revision, and
   freshness; do not copy whole source records into the packet.
3. Decide whether a material signal exists. If not, record a bounded
   no-material-signal result or hold with the missing condition.
4. Create the `SignalPacket` before any substantial prose: observation,
   reconstruction, claim, evidence, warrant, counterclaim or uncertainty,
   boundaries, significance, next move, approval, and publication state.
5. Check that the claim is warranted, the sensitivity is correct, the
   audience is named, and truth conditions will survive translation.
6. Produce only packet-linked audience projections. Hold, narrow, request
   evidence, or escalate when authority, provenance, freshness, permission,
   or reviewer independence is insufficient.
7. Request packet-linked review, approval, reconciliation, or follow-up
   through the approved control-plane workflow. Do not route work, assign
   capacity, or silently rewrite a source system.
8. Record reception, correction, supersession, and capability-harvest links
   without deleting the original packet or source provenance.

## Boundaries

Do not change project status, priority, owner, assignee, completion, canonical
memory, evaluator results, constitutional precedent, or capability records to
improve a story. Do not publish restricted information, create commitments,
run general communications, route work, allocate capacity, or treat external
discovery as institutional fact before its evaluation path is complete. Do not
use engagement, publication volume, or polished tone as evidence.

When records conflict, preserve the conflict and request reconciliation from
the owning control-plane or record authority. When an action would be public,
leadership-facing, external, restricted, or commitment-bearing, require the
applicable human or specialist approval.

## Verification

Run `python scripts/validate_package.py` and
`python -m unittest discover -s tests -v`. Passing proves local package
structure and fixture behavior only; it does not establish installation,
promotion, runtime registration, authorization, publication, or production
readiness.
