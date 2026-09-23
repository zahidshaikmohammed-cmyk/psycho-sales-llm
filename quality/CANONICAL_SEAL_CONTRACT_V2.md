# PSYCHO SALES — CANONICAL SEAL CONTRACT v2.0

**Status:** LOCKED — EXECUTABLE GOVERNANCE CONTRACT  
**Authority:** This contract operationalizes the Permanent Knowledge Object Writer Constitution v2.0.  
**Purpose:** Define the minimum evidence required before a chapter may claim **LOCKED & SEALED**.

## 1. Separation of machine checks and expert judgments

A canonical seal requires BOTH:

1. **Machine gates** executed by `quality/validate_canonical_chapter.py`.
2. **Semantic audit attestation** recorded in the chapter's final validation file.

Neither layer substitutes for the other.

The machine validator must never pretend to determine scientific truth from prose alone. The attestation must never substitute for mechanical ontology or structural checks.

## 2. Mandatory machine gates

The validator must fail a seal when any of the following fails:

- chapter architecture exists and is uniquely identifiable;
- chapter Topic count matches architecture;
- Topic IDs and names match architecture exactly;
- no added, removed, or renamed Topic is present;
- six permanent sections exist in exact order for every Topic;
- Owns and Defers boundaries are present and non-empty;
- Topic blocks are non-empty;
- duplicate Topic IDs do not occur;
- duplicate Topic names within a chapter do not occur;
- placeholder/template signatures are absent;
- repeated Core Understanding blocks are absent;
- repeated Relationship blocks are absent;
- repeated Key-Principle sets are absent;
- generic chapter-membership prose is absent from Topic-specific fields;
- obvious sales/persuasion contamination is absent from System 1 canonical prose;
- validation attestation is present and internally consistent.

## 3. Mandatory v2 semantic attestation

The final validation record must contain a section titled:

`## V2 Semantic Gate — Required for Canonical Seal`

It must report PASS/FAIL for:

- Ontology match
- Structural integrity
- Ownership
- Semantic depth
- Neighbor distinctions
- Scientific/evidence integrity
- Relationships
- Retrieval
- Anti-template
- Cross-chapter boundaries
- Final validation

It must also report integer counts for:

- P0
- P1
- P2
- P3

Canonical seal requires:

- P0 = 0
- P1 = 0
- P2 = 0 unless explicitly justified in the same record
- all ten gate lines = PASS
- final validation = PASS

## 4. No retrospective laundering

An older validation record cannot become v2-compliant merely because this contract exists.

A chapter previously marked LOCKED & SEALED remains historically sealed until it is actually re-certified under v2.

## 5. Versioning

A v2-certified chapter must identify its canonical knowledge version and the date of v2 certification.

The validator checks the seal contract; it does not rewrite historical versions.

## 6. Enforcement principle

> **No executable pass + no valid v2 attestation = no new canonical seal.**

This contract governs future sealing immediately. Retroactive chapter re-certification remains a separate remediation phase.