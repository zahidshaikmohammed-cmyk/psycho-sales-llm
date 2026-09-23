# PSYCHO SALES — SEMANTIC DEPTH AUDIT PROTOCOL v1.0

## Purpose
Determine whether a canonical Knowledge Object is genuinely complete rather than merely structurally compliant.

## Required audit dimensions
1. Identity — uniquely identifiable concept.
2. Definition — precise and non-circular.
3. Distinction — nearest neighbors separated.
4. Mechanism — relevant process logic without invented causality.
5. Scope — included and excluded phenomena clear.
6. Forms — major variants covered where materially relevant.
7. Conditions — antecedents, moderators, constraints, and boundary conditions.
8. Temporal structure — state/process/trait and timing distinctions where relevant.
9. Context — context-dependent effects.
10. Individual variation — meaningful differences without deterministic overclaiming.
11. Measurement — construct separated from operationalization and measurement.
12. Evidence — empirical claims proportioned to evidence.
13. Uncertainty — unresolved questions visible.
14. Misconception resistance — common category errors prevented.
15. Relationships — important cross-concept relationships represented.
16. Ownership — canonical ownership unambiguous.
17. Retrieval — natural-language variants retrieve reliably.
18. Anti-template — prose is genuinely Topic-specific.
19. Application boundary — downstream application cannot contaminate universal psychology.
20. Human readability — intelligent non-specialists can understand it without loss of precision.

## Severity
P0 = canonical integrity failure: wrong Topic, duplicate owner, material falsehood, fabricated certainty, architecture conflict.
P1 = major semantic gap: missing central mechanism, major conceptual confusion, consequential evidence limitation absent.
P2 = meaningful completeness gap: missing important variant, context, individual difference, measurement distinction, or relationship.
P3 = refinement: terminology, alias, example, or wording improvement.

P0/P1 block sealing. P2 blocks high-confidence canonical status unless explicitly justified.

## Anti-template tests
Explicitly test for literal placeholders, repeated Core Understanding paragraphs, repeated Relationship sections, repeated Key-Principle sets, generic chapter-membership language, and fixed templates with Topic-name substitution.

## Neighbor test
For every Topic identify the most important neighboring concepts and ask: if an LLM retrieved either Topic, could it explain why the two are different? If not, remediate.

## Evidence test
For each substantive empirical claim classify it as definition, descriptive evidence, association, causal evidence, theoretical interpretation, contested claim, or unresolved question. Do not collapse categories.

## Relationship test
Where meaningful, relationships should be typed as influences, predicts, mediates, moderates, constrains, enables, depends_on, precedes, follows, interacts_with, competes_with, dissociates_from, measured_by, supported_by, challenged_by, and similar relation classes.

## Seal output
Every final validation record should report Topic count, ontology match, structural compliance, ownership, semantic audit, P0/P1/P2/P3 counts, template findings, neighbor distinctions, evidence integrity, retrieval findings, cross-chapter findings, and final seal decision.

> A Topic does not pass because it has six sections. It passes because a reader or machine can use the knowledge correctly without importing hidden assumptions.

## Executable enforcement

Phase 2 adds executable enforcement through:

- `quality/CANONICAL_SEAL_CONTRACT_V2.md` — binding seal requirements.
- `quality/validate_canonical_chapter.py` — deterministic ontology, structure, ownership-boundary, anti-template, duplication, depth-floor, and attestation checks.
- `quality/V2_SEMANTIC_ATTESTATION_TEMPLATE.md` — required expert-audit record.
- `.github/workflows/canonical-quality-v2.yml` — pull-request and branch CI enforcement.
- `quality/tests/test_validate_canonical_chapter.py` — validator self-tests.

The executable layer intentionally does not claim to infer scientific truth, neighbor distinctions, or evidence quality from text automatically. Those remain explicit semantic-audit attestations governed by this protocol.

## Phase 2 sealing rule

A newly changed canonical chapter or validation record cannot pass the v2 CI gate without a valid v2 semantic attestation. Existing historical seals are not retroactively re-certified by the infrastructure change.