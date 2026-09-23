# PSYCHO SALES — PSYCHOLOGICAL KNOWLEDGE GRAPH SPECIFICATION v1.0

## Purpose
The canonical prose corpus is the human-readable knowledge layer. This specification defines the relationship layer required for future intelligence systems.

## Node classes
construct; process; mechanism; state; phenomenon; individual_difference; theory_model; method_measurement; clinical_condition; relationship_application; chapter; system.

## Relationship classes
is_a; part_of; subtype_of; distinct_from; overlaps_with; influences; influenced_by; predicts; predicted_by; mediates; moderated_by; moderates; constrains; enables; depends_on; precedes; follows; interacts_with; competes_with; dissociates_from; measured_by; operationalized_by; supported_by; challenged_by; applied_to; specializes; generalizes_to; defers_to; owned_by.

## Relationship record
A machine-readable relationship should support source Topic ID, target Topic ID, relationship type, direction, scope/context, evidence status, uncertainty, notes, source references, date, and version.

## Example
Attention influences Encoding under task-dependent conditions. The relationship is substantial but not deterministic; the direction and scope must remain explicit.

## Critical rule
A relationship node is not automatically an independent construct. The graph must preserve the ontology's single-owner principle.

## Graph quality target
The eventual system should answer not only what a concept is, but what it interacts with, under what conditions, what effects are established versus theoretical, and which concepts are commonly confused with it.

The graph is a reasoning substrate, not merely a bibliography.
