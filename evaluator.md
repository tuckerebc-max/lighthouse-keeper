# Lighthouse Evaluator and Acceptance Tests

## Communication lint

Before approval, check:

- every material claim links to a stable source;
- source authority, revision, and time window are clear;
- observation, interpretation, hypothesis, aspiration, and commitment are
  distinct;
- the warrant explains why the evidence supports the claim;
- contradictions, failed attempts, regressions, and uncertainty are visible;
- the audience and sensitivity are named;
- the projection does not imply an unsupported result, endorsement, or
  commitment;
- the next move is specific;
- a future reviewer can reconstruct the decision without reopening the
  original conversation;
- the artifact is a projection of a packet, not standalone general
  communications or routing work.

## Rubric

Score each dimension 0–2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Fidelity | Unsupported or distorted | Mostly accurate with gaps | Faithful and source-traceable |
| Significance | Activity dump | Some implication | Explains meaningful institutional change |
| Warrant | Assertion only | Evidence named but reasoning weak | Evidence and reasoning are explicit |
| Calibration | Overclaiming or vague | Some limits | Clear uncertainty and scope |
| Audience fit | Misaligned | Understandable | Emphasis changes without truth drift |
| Direction | No consequence | Generic next step | Specific decision, test, build, or invitation |
| Boundaries | Permission risk | Ambiguity | Correct sensitivity and authority handling |
| Memory value | Disposable | Some links | Reusable, versioned, correctable record |

Material public or leadership projections should score 2 on Fidelity, Warrant,
Calibration, and Boundaries, and at least 12/16 overall. A reviewer may hold a
packet regardless of score.

## Architecture acceptance tests

The package is behaviorally coherent when an evaluator can demonstrate that:

- a material change can be traced into a `SignalPacket`;
- the packet contains claim, evidence, warrant, uncertainty, boundary,
  audience, and next move;
- distinct audience projections preserve the claim's truth conditions;
- insufficient evidence produces a hold, evidence request, evaluation
  candidate, or no-material-signal note;
- corrections and supersession preserve prior provenance;
- a closeout can link a capability harvest;
- no packet action assigns work, routes capacity, or mutates canonical records.

The package validator and fixtures check structural versions of these tests.
They do not authorize publication, installation, promotion, runtime
registration, or external writes.
