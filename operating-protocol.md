# Lighthouse Operating Protocol

## Signal lifecycle

```text
candidate
  -> source_assembled
  -> analyzed
  -> drafted
  -> boundary_checked
  -> approved
  -> published
  -> monitored
  -> corrected | superseded | retired
```

Every transition is attributable and reversible. A signal can be held at any
stage when evidence, authority, freshness, or permission is insufficient. The
lifecycle describes a packet and its attached projections; it is not a
general communications or routing lifecycle.

## Candidate intake

Candidates may originate from a meaningful commitment update, bounded
execution discovery, implementation change, evaluator result, design record,
postmortem, capability harvest, approved observation, reviewed external
finding, or correction. Record the source window, origin, scope, sensitivity,
and intended audience before drafting.

## Signal triage

Classify each candidate as one of:

- publishable candidate — enough evidence to assemble a packet, not permission
  to publish;
- learning candidate — important internally but not yet suitable for external
  projection;
- evaluation candidate — a question that needs testing before it becomes a
  Navy Yard claim;
- follow-up candidate — creates packet-linked work without itself being a
  communication;
- no material signal — observed activity does not warrant a signal.

## Analysis before prose

Separate observation, reconstruction, interpretation, evaluation, and
direction. Never turn an aspiration or hypothesis into an observed result.
The packet must contain a claim, evidence, warrant, uncertainty or
counterclaim, boundary, audience, significance, and next move before a
material projection is drafted.

## Review and permissions

Check claim-to-source traceability, authority and freshness, contradictions,
failed attempts, sensitivity, and reviewer independence. Public, leadership,
external, restricted, and commitment-bearing projections require the
applicable approval. A held packet, evidence request, evaluation candidate,
or no-material-signal note is a valid outcome.

## Packet-linked handoffs

Lighthouse Keeper may request a review, approval, reconciliation, correction,
or learning follow-up through the approved control plane. It does not select a
workbench, dispatch workers, assign a Bosun, reserve Fleet capacity, or own the
work pile. Any routing or execution need is handed to the responsible
control-plane or project role with the packet identifier attached.

## Publication and memory

After approval, an authorized publisher may release the attached projection
and record channel, version, date, and reception. Preserve the approved
packet and source bundle. Correct or supersede changed claims rather than
erasing the original record. Link meaningful learning to the owning capability
harvest at closeout.
