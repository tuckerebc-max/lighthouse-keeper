# Lighthouse Keeper

Lighthouse Keeper is the Navy Yard's candidate skill for compiling warranted
`SignalPacket` records from meaningful, evidence-bearing Work Graph changes.
The Signal Packet is the package's only primary record. Audience-specific
briefs, reports, or public drafts are derived projections of an existing
packet; they are not independent communications work.

## Identity and boundary

| Field | Value |
|---|---|
| Skill/package | `lighthouse-keeper` |
| Role | `navy-yard.lighthouse-keeper` |
| Version | `0.1.0` candidate |
| Primary record | `SignalPacket` |
| Default publication | Disabled; approval is required |
| Routing authority | None |

Lighthouse Keeper does not operate a general communications calendar, route
work, assign workers, allocate capacity, or mutate canonical Linear, Beads,
Notion, GitHub, evaluator, or policy records. It may request a packet-linked
review or follow-up through the approved control plane, but it does not become
the routing or execution function.

## Use

Invoke explicitly as `$lighthouse-keeper` when a bounded reporting window may
contain a material milestone, capability gain, learning, decision,
failure/repair, direction, boundary, invitation, correction, or explicit
no-material-signal result.

The workflow is:

`authorized sources -> Signal Packet -> boundary review -> approved projection -> reception/correction -> learning link`

No packet means no material outward prose. Activity alone is not a signal.

## Package contents

- `SKILL.md` — concise operating procedure and boundaries.
- `manifest.json` — package identity, authority fence, references, and provenance.
- `references/role-specification.md` — source-aligned role contract.
- `schemas/signal-packet.schema.json` — machine-readable packet contract.
- `schemas/package-manifest.schema.json` — package manifest contract.
- `references/evaluator.md` — acceptance rubric and architecture checks.
- `examples/` — valid and held packet fixtures.
- `agents/openai.yaml` — OpenAI/Codex discovery metadata.

## Verification

Use Python 3.11 or later with an environment outside this package. From this
package directory, install the pinned dependencies and run:

```text
python -m pip install -r requirements.txt
python -B scripts/validate_package.py
python -B -m unittest discover -s tests -v
```

The `-B` flag prevents test imports from creating bytecode files that the
package's debris check rejects. Manifest file references and metadata icons
must use forward-slash relative paths to files inside the package.

Passing these checks establishes package integrity only. It does not install,
promote, register, activate, publish, or certify the skill for production.

## Provenance

This candidate reconciles the supplied Lighthouse Keeper package, the local
role specification, the local role manifest, and the local source review. The
source repository revision recorded in `manifest.json` is evidence, not an
activation claim.
