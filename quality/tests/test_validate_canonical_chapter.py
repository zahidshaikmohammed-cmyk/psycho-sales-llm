import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'quality'))
import validate_canonical_chapter as validator

ATTEST = '''
## V2 Semantic Gate — Required for Canonical Seal
- Ontology match: PASS
- Structural integrity: PASS
- Ownership: PASS
- Semantic depth: PASS
- Neighbor distinctions: PASS
- Scientific/evidence integrity: PASS
- Relationships: PASS
- Retrieval: PASS
- Anti-template: PASS
- Cross-chapter boundaries: PASS
- Final validation: PASS
- P0: 0
- P1: 0
- P2: 0
- P3: 0
'''

def chapter(include_attestation=True):
    body = ('This concept is described with enough concept-specific detail to clear the executable semantic floor. ' * 8).strip()
    return '''# CHAPTER 9.9 — TEST
**Canonical Topic count:** 1

## 9.9.1 Example construct
## 1. Purpose
Explain the example construct.
## 2. Definition
The example construct is a defined psychological object.
## 3. Core Understanding
''' + body + '''
## 4. Relationship to This Chapter
It is the chapter's canonical object.
## 5. Boundaries
### Owns
Owns the example construct.
### Defers
Defers unrelated constructs.
## 6. Key Principles
- The construct has a defined scope.
- The construct is not a placeholder.
''' + (ATTEST if include_attestation else '')

class ValidatorTests(unittest.TestCase):
    def test_valid_object_passes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'chapter.md').write_text(chapter(),encoding='utf-8')
            (p/'architecture.md').write_text('# CHAPTER 9.9 — TEST\n- Example construct\n',encoding='utf-8')
            (p/'validation.md').write_text(ATTEST,encoding='utf-8')
            self.assertEqual(validator.validate(p/'chapter.md',p/'architecture.md',p/'validation.md'), [])

    def test_missing_attestation_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'chapter.md').write_text(chapter(False),encoding='utf-8')
            (p/'architecture.md').write_text('# CHAPTER 9.9 — TEST\n- Example construct\n',encoding='utf-8')
            (p/'validation.md').write_text('',encoding='utf-8')
            errors=validator.validate(p/'chapter.md',p/'architecture.md',p/'validation.md')
            self.assertTrue(any('attestation' in e for e in errors))

if __name__ == '__main__': unittest.main()