# SYSTEM 1 — ARCHITECTURE PRECISION REGISTRY

**Status:** PRECISION PASS — MACHINE-AUDITABLE EXCEPTION LEDGER  
**Source architecture:** `system_1/SYSTEM_1_SURGICAL_CANONICAL_ARCHITECTURE_v2.md`  
**Purpose:** Make the chapter-entry count and canonical-owner count reproducible without silently changing locked Topic names.

---

## 1. Counting contract

The architecture contains **1,364 chapter architecture entries**.

The count is now defined mechanically as:

- all Topic/redirect bullets belonging to Chapters 1.1–1.21;
- Chapter 1.21 ends after its 37 core ontology entries plus 8 explicit redirects;
- global relationship, model-registry, application-boundary, clinical-separation, and audit prose after that boundary are **not** Chapter 1.21 Topics.

### Canonical construct/clinical owner count

`1,364 - 60 - 12 - 9 - 16 = 1,267`

Where:

- **60** = relationship/application nodes; useful contextual nodes, not independent owners.
- **12** = duplicate-name non-owner appearances resolved to an existing canonical owner.
- **9** = explicit redirects; pointers, not owners.
- **16** = theory/model entries; retained in the Theory / Model Registry and not counted as independent construct/clinical owners in the 1,267 owner metric.

**Important:** The 1,267 metric is therefore specifically the **canonical construct/clinical owner count**. The Theory / Model Registry remains a separate canonical layer.

---

## 2. Chapter-entry counts

| Chapter | Chapter architecture entries |
|---|---:|
| 1.1 | 57 |
| 1.2 | 118 |
| 1.3 | 78 |
| 1.4 | 62 |
| 1.5 | 44 |
| 1.6 | 40 |
| 1.7 | 66 |
| 1.8 | 76 |
| 1.9 | 67 |
| 1.10 | 65 |
| 1.11 | 60 |
| 1.12 | 75 |
| 1.13 | 62 |
| 1.14 | 67 |
| 1.15 | 62 |
| 1.16 | 101 |
| 1.17 | 53 |
| 1.18 | 58 |
| 1.19 | 64 |
| 1.20 | 44 |
| 1.21 | 45 |
| **TOTAL** | **1,364** |

Chapter 1.21 therefore has **37 core ontology entries + 8 explicit redirects = 45 chapter entries**.

---

## 3. Relationship / application nodes — 60

These entries remain visible for retrieval/context but do not create independent canonical construct owners.

1. 1.1 — General principles and individual variation
2. 1.3 — Brain injury and psychological function
3. 1.5 — Sleep and learning
4. 1.5 — Sleep and emotion
5. 1.7 — Feedback and learning
6. 1.7 — Learning and context
7. 1.8 — Memory and identity
8. 1.8 — Emotion and memory
9. 1.8 — Stress and memory
10. 1.8 — Sleep and memory
11. 1.9 — Expertise and thinking
12. 1.10 — Moral judgment and decision-making
13. 1.11 — Language and thought
14. 1.11 — Language and memory
15. 1.11 — Language and attention
16. 1.11 — Language and executive control
17. 1.11 — Working memory and intelligence
18. 1.11 — Intelligence and heredity
19. 1.11 — Intelligence and environment
20. 1.11 — Intelligence and education
21. 1.11 — Intelligence and problem solving
22. 1.11 — Intelligence and creativity
23. 1.12 — Motivation and context
24. 1.13 — Emotion and cognition
25. 1.8 — Emotion and memory
26. 1.13 — Emotion and attention
27. 1.13 — Emotion and decision-making
28. 1.13 — Emotion and motivation
29. 1.13 — Emotion and action
30. 1.13 — Emotion and social judgment
31. 1.15 — School and learning context
32. 1.16 — Attitude–behavior relationship
33. 1.16 — Attachment in adult relationships
34. 1.16 — Empathy–altruism relationship
35. 1.17 — Cross-cultural differences
36. 1.17 — Cultural variation in emotion
37. 1.17 — Cultural variation in cognition
38. 1.17 — Cultural variation in motivation
39. 1.17 — Cultural variation in personality
40. 1.17 — Cultural variation in social relationships
41. 1.17 — Cultural variation in moral judgment
42. 1.17 — Culture and perception
43. 1.17 — Culture and development
44. 1.17 — Culture and health
45. 1.17 — Language and culture
46. 1.17 — Measurement invariance across cultures
47. 1.17 — Generalizability across cultures
48. 1.18 — Physical health and behavior
49. 1.18 — Exercise and psychological function
50. 1.18 — Nutrition and psychological function
51. 1.18 — Sleep and health
52. 1.18 — Substance use and health
53. 1.4 — Individual differences in perception
54. 1.8 — Individual differences in memory
55. 1.11 — Individual differences in intelligence
56. 1.13 — Individual differences in emotion
57. 1.19 — Biological factors in psychopathology
58. 1.19 — Psychological factors in psychopathology
59. 1.20 — Informed consent in treatment
60. 1.20 — Cultural adaptation of treatment

---

## 4. Duplicate-name non-owner appearances — 12

These are exact-name appearances whose canonical owner is elsewhere.

1. 1.21 — Behavior → canonical owner 1.1
2. 1.1 — Individual differences → canonical owner 1.14
3. 1.1 — Psychological flexibility → canonical owner 1.18
4. 1.1 — Action → canonical owner 1.21
5. 1.1 — Self-regulation → canonical owner 1.12
6. 1.20 — Confidentiality → canonical owner 1.2
7. 1.9 — Bounded rationality → canonical owner 1.10
8. 1.16 — Group decision-making → canonical owner 1.10
9. 1.11 — Emotional intelligence → canonical owner 1.13
10. 1.14 — Personality development → canonical owner 1.15
11. 1.16 — Stigma → canonical owner 1.19
12. 1.19 — Early intervention → canonical owner 1.20

---

## 5. Explicit redirects — 9

1. 1.14 — Attachment style → 1.15 canonical owner (redirect only)
2. 1.21 — Reinforcement → 1.7
3. 1.21 — Motivation → 1.12
4. 1.21 — Self-control → 1.12
5. 1.21 — Habit formation → 1.7
6. 1.21 — Personality → 1.14
7. 1.21 — Social behavior → 1.16
8. 1.21 — Skill learning → 1.7
9. 1.21 — Emotion regulation → 1.13

Redirects are navigation pointers only. They never create a second owner.

---

## 6. Theory / model registry entries excluded from the construct/clinical owner metric — 16

1. 1.1 — Dynamic-systems perspective
2. 1.10 — Rational choice models
3. 1.10 — Expected utility theory
4. 1.10 — Prospect theory
5. 1.10 — Dual-process accounts
6. 1.12 — Drive-reduction theory
7. 1.12 — Arousal theory
8. 1.12 — Incentive theory
9. 1.12 — Self-determination theory
10. 1.12 — Expectancy-value theory
11. 1.13 — James–Lange theory
12. 1.13 — Cannon–Bard theory
13. 1.13 — Two-factor theory
14. 1.13 — Cognitive appraisal theories
15. 1.13 — Basic-emotion approaches
16. 1.13 — Constructed-emotion approaches

These remain canonical theory/model knowledge and are governed by the Theory / Model Registry. They are excluded from the 1,267 **construct/clinical owner** metric so the metric does not mix ontology layers.

---

## 7. Controlled ontology types

Every chapter entry must ultimately resolve to exactly one primary type:

1. Construct
2. Process
3. Mechanism
4. State
5. Phenomenon
6. Individual difference
7. Theory/model
8. Method/measurement object
9. Clinical condition
10. Application/relationship

The precision rule is:

- **Theory/model** → registry-owned and excluded from the construct/clinical owner metric.
- **Application/relationship** → contextual node and excluded from independent-owner count.
- **Redirect** → navigation metadata and excluded from independent-owner count.
- **Duplicate appearance** → points to the canonical owner and excluded from independent-owner count.
- All remaining chapter entries → one independent canonical owner, with one primary ontology type.

No Topic name is changed by this registry.

---

## 8. Machine-audit rule

A future audit must reproduce the following without interpretation:

`chapter_entries = 1,364`

`relationship_application = 60`

`duplicate_aliases = 12`

`redirects = 9`

`theory_model_registry_entries_in_chapter_lists = 16`

`canonical_construct_clinical_owners = 1,267`

If any number changes, the architecture must be re-audited before the lock state is changed.

---

## 9. Precision-pass result

**COUNTING / OWNERSHIP ACCOUNTING: REPRODUCIBLE**

This registry does not silently rewrite sealed chapter prose or rename locked Topics. It formalizes the previously implicit exclusions and establishes the counting contract for future architecture audits.
