import re
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import review_craft_features as craft  # noqa: E402
import check_review_craft as gate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def _pad(text: str, words: int = 4200) -> str:
    """Pad *body* words so the 4,000-word floor cannot skip the gate.

    Filler must sit before References. Appending after the list leaves
    body_before_references() short, and craft_problems() returns [].
    """
    filler = " Pressure acts throughout the pack so piece size does not create a cold spot."
    extra = []
    n = len(text.split())
    while n < words:
        extra.append(filler)
        n += len(filler.split())
    block = "\n\n" + "".join(extra) + "\n\n"
    marker = re.search(r"(?im)^(?:##\s+)?References\s*$", text)
    if marker:
        return text[: marker.start()] + block + text[marker.start() :]
    return text + block


GOOD = """# Phenomenon: a narrative review of a tension

## Abstract
Heat is the default kill step, yet it cooks flavour. Pressure offers another hold. Vegetative cells often die; spores often do not. Those patterns do not imply a sterility claim.

## Keywords
pressure; spores; pasteurisation; quality

## 1. Introduction
Heat remains the kill step that most plants assume. Current time–temperature cycles already meet legal milk pasteurisation, yet they destroy the colour a puree is sold for. Pressure can reduce vegetative counts without that cook, however it does not inactivate bacterial spores at ambient industrial settings.
The aim of this review is to show when a labelled hold is a vegetative hurdle and when it is not.

## 2. Methods
### 2.1 Search and sources
Public full texts were opened.
### 2.2 Eligibility
Human food and inactivation studies.
### 2.3 Study selection
Forty-three studies were included.

## 3. Why the same hold is not the same kill
Because lethality depends on ice and solute, those coefficients are not footnotes.

### 3.1 Ice versus liquid packs
Unfrozen buffer lost 1.83 log after 400 MPa for 9 min, whereas the same hold after freezing reached 6.83 log [1]. Kinetic compilations report the same direction in juices [2,3]. Taken together, ice is a coefficient, not a general licence to drop industrial pressure. This heading cannot show a STEC validation.

### 3.2 Water activity
Undiluted honey at 600 MPa and 85 °C left spores unchanged [4]. Diluted honey at 75 °C fell to the detection limit [4,5]. These data suggest the continuous phase, not the megapascal sticker, sets the spore outcome.

### 3.3 Injury and agar
Immediate plates in banana–apple puree recorded 0.3 log Listeria; delayed sampling and acid exposure raised that number [6]. Several juice trials that look like 5-log events counted indigenous aerobes rather than named pathogens [7,8]. Taken together, the assay manufactures part of the log.

## 4. Legal bars versus measured logs
### 4.1 Milk
An expert opinion concludes that non-thermal pressure cannot match legal thermal pasteurisation of ruminant milk [9]. A mixed-model review places Staphylococcus aureus near 600 MPa for a greater-than-five-log average [10]. Overall, those are performance criteria, not vessel stickers.

## 8. Discussion
The pattern is a long causal chain from named hold to assay to legal sentence. What cannot currently be concluded is a paired 72 °C trial on S. aureus in milk.

## 9. Conclusions
Ambient pressure is a refrigerated vegetative tool in high-moisture foods. It is not a sterility certificate.

## References
[1] A. Title. 2021.
"""

BAD = """# High-pressure processing of foods: a narrative review of when a named cycle is not one outcome

## Abstract
This review discusses pressure.

## 1. Introduction
This review discusses included papers. The aim of this review is to list them.

## 2. Methods
### 2.1 Search
Scopus.

## 3. Results
A named cycle is not one outcome. A named cycle is not one outcome. A named cycle is not one outcome.
In this sample, Smith 2021 treated juice at 400 MPa (n = 3) and found 2 log CFU [1].
In this sample, Jones 2022 treated milk at 600 MPa (n = 3) and found 5 log CFU [2].
The intellectual model that survives this sample is a catalogue. A named cycle is not one outcome.

## Discussion
In this set the papers disagree.

## References
[1] Smith. 2021.
"""


class FeatureTests(unittest.TestCase):
    def test_good_has_nests_and_cars(self):
        f = craft.extract_craft_features(GOOD)
        self.assertGreaterEqual(f["nested_thematic_h3"], 3)
        self.assertEqual(f["cars_niche_before_aim"], 1.0)
        self.assertLess(f["meta_reviewer_hits"], 2)
        self.assertGreater(f["thematic_synthesis_frac"], 0.4)

    def test_bad_is_flat_and_meta(self):
        f = craft.extract_craft_features(BAD)
        self.assertLess(f["nested_thematic_h3"], 3)
        self.assertGreaterEqual(f["meta_reviewer_hits"], 2)
        self.assertGreaterEqual(f["slogan_hits"], 3)
        self.assertEqual(f["cars_niche_before_aim"], 0.0)


class GateTests(unittest.TestCase):
    def test_padded_good_passes(self):
        problems = gate.craft_problems(_pad(GOOD), short=False)
        self.assertEqual(problems, [], problems)

    def test_padded_bad_fails_nests_and_meta(self):
        problems = gate.craft_problems(_pad(BAD), short=False)
        joined = " ".join(problems).lower()
        self.assertTrue(any("nested" in p.lower() for p in problems), problems)
        self.assertTrue("meta-reviewer" in joined or "slogan" in joined, problems)

    def test_short_skips(self):
        self.assertEqual(gate.craft_problems(BAD, short=True), [])

    def test_cli_on_good_fixture_is_short_enough_to_skip(self):
        # good-article.md is under 4000 words so the CLI exits 0 even without nests
        from unittest.mock import patch
        import sys as _sys

        path = str(ROOT / "tests/fixtures/good-article.md")
        with patch.object(_sys, "argv", ["check_review_craft.py", "--article", path]):
            self.assertEqual(gate.main(), 0)


class SkillTests(unittest.TestCase):
    def test_skill_exists(self):
        path = ROOT / ".cursor/skills/review-writing-craft/SKILL.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        self.assertIn("CASRAI", text)
        self.assertIn("CARS", text)
        self.assertIn("Gopen", text)
        self.assertIn("Pautasso", text)
        self.assertIn("hinge", text.lower())
        self.assertIn("Do not import", text)


class LiveManuscriptTests(unittest.TestCase):
    def test_houska_nests_more_than_hpp_rerun(self):
        houska = ROOT / "papers/2026-09-20-hpp-rerun/Houška2022_020223.txt"
        ours = ROOT / "review/runs/2026-09-20-hpp-rerun/article.md"
        if not houska.is_file() or not ours.is_file():
            self.skipTest("published comparator or rerun article missing")
        published = craft.extract_from_path(houska)
        draft = craft.extract_from_path(ours)
        self.assertGreaterEqual(published["nested_thematic_h3"], 8)
        self.assertLess(draft["nested_thematic_h3"], 3)

    def test_scopus_hpp_v1_has_thematic_nests(self):
        path = ROOT / "review/runs/2026-09-20-scopus-hpp/article.md"
        if not path.is_file():
            self.skipTest("v1 HPP article missing")
        feats = craft.extract_from_path(path)
        self.assertGreaterEqual(feats["nested_thematic_h3"], 8)
