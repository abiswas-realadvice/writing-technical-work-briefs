"""Deterministic tests for the design-element checker.

These tests take no network access, spawn no model, and cost nothing to
run. Each "bad-*" fixture is a minimal HTML document that deliberately
violates exactly one design rule from
skills/executive-brief/reference/design-and-visuals.md; each test asserts
the checker flags that specific rule. The "good" fixtures are the two
templates shipped with the skill -- one-page and five-page -- and each
must pass every rule; if a future edit to a template or the checker
breaks that, this test suite fails. bad-multi-page-heading.html proves
the per-page heading rule still catches a real violation once a document
has more than one page, not just that it stops flagging a legitimate one.

good-inline-style-and-units.html pins down three fixes found by testing
the checker against real, independently-authored executive documents
(not synthetic fixtures written to already match the convention): an
element's own inline style="..." must win over a same-property class
rule (real brief HTML very commonly sets a per-instance background this
way, e.g. severity-colored chips), non-pt length units (rem here) must
resolve correctly for body text size, and an anchor reached through a
descendant selector like ".sub a" must still count as a link selector
for the underline rule.

Run with:
    python3 -m unittest discover -s tests -v
or, if pytest is available:
    pytest tests/
"""

import contextlib
import importlib.util
import io
import pathlib
import sys
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKER_PATH = REPO_ROOT / "skills" / "executive-brief" / "scripts" / "check_brief_design.py"
ASSETS_DIR = REPO_ROOT / "skills" / "executive-brief" / "assets"
TEMPLATE_PATH = ASSETS_DIR / "one-page-brief-template.html"
FIVE_PAGE_TEMPLATE_PATH = ASSETS_DIR / "five-page-brief-template.html"
FIXTURES_DIR = pathlib.Path(__file__).resolve().parent / "fixtures"


def _load_checker():
    spec = importlib.util.spec_from_file_location("check_brief_design", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # dataclass needs this registered before exec_module
    spec.loader.exec_module(module)
    return module


checker = _load_checker()


def run_on(path):
    return checker.check(path.read_text(encoding="utf-8"))


def failing_ids(results):
    return {r.rule_id for r in results if not r.passed}


class GoodBriefPassesEveryRule(unittest.TestCase):
    # Both the single-page brief and the five-page paper must pass cleanly --
    # this is what proves the convention and the checker aren't one-pager-only.
    TEMPLATES = {
        "one-page": TEMPLATE_PATH,
        "five-page": FIVE_PAGE_TEMPLATE_PATH,
    }

    def test_templates_pass_all_rules(self):
        for label, path in self.TEMPLATES.items():
            with self.subTest(template=label):
                results = run_on(path)
                self.assertEqual(
                    failing_ids(results),
                    set(),
                    f"the shipped {label} template should pass every design rule",
                )
                self.assertEqual(len(results), 13, "expected all 13 design rules to run")

    def test_inline_style_and_units_fixture_passes(self):
        results = run_on(FIXTURES_DIR / "good-inline-style-and-units.html")
        self.assertEqual(failing_ids(results), set())


class EachBadFixtureIsCaught(unittest.TestCase):
    # fixture filename -> rule ID(s) it must trip
    CASES = {
        "bad-heading-hierarchy.html": {"DES-1"},
        "bad-heading-allcaps.html": {"DES-2"},
        "bad-alt-text.html": {"DES-3"},
        "bad-contrast.html": {"DES-4"},
        "bad-underline.html": {"DES-5"},
        "bad-table.html": {"DES-6", "DES-7"},
        "bad-chart.html": {"DES-8", "DES-9"},
        "bad-status.html": {"DES-10"},
        "bad-fontsize.html": {"DES-11"},
        "bad-footer.html": {"DES-12"},
        "bad-palette.html": {"DES-13"},
        "bad-multi-page-heading.html": {"DES-1"},
    }

    def test_every_fixture_exists(self):
        for filename in self.CASES:
            self.assertTrue((FIXTURES_DIR / filename).is_file(), f"missing fixture {filename}")

    def test_each_fixture_trips_its_rule(self):
        for filename, expected in self.CASES.items():
            with self.subTest(fixture=filename):
                results = run_on(FIXTURES_DIR / filename)
                failed = failing_ids(results)
                self.assertTrue(
                    expected.issubset(failed),
                    f"{filename}: expected {expected} to fail, but only {failed} failed",
                )

    def test_each_fixture_trips_only_its_rule(self):
        # Every fixture is built from an otherwise-compliant skeleton, so
        # nothing outside the targeted rule(s) should fail. This catches
        # accidental over-broad checks as well as fixtures that drifted
        # out of sync with the convention.
        for filename, expected in self.CASES.items():
            with self.subTest(fixture=filename):
                results = run_on(FIXTURES_DIR / filename)
                failed = failing_ids(results)
                self.assertEqual(
                    failed,
                    expected,
                    f"{filename}: expected exactly {expected} to fail, got {failed}",
                )


class CoreHelpersAreCorrect(unittest.TestCase):
    def test_contrast_ratio_black_on_white_is_maximal(self):
        ratio = checker.contrast_ratio("#000000", "#ffffff")
        self.assertAlmostEqual(ratio, 21.0, places=1)

    def test_contrast_ratio_identical_colors_is_one(self):
        ratio = checker.contrast_ratio("#336699", "#336699")
        self.assertAlmostEqual(ratio, 1.0, places=6)

    def test_is_grayscale_true_for_neutral_gray(self):
        self.assertTrue(checker.is_grayscale("#d6d6d9"))

    def test_is_grayscale_false_for_saturated_color(self):
        self.assertFalse(checker.is_grayscale("#0b5fff"))

    def test_is_large_text_thresholds(self):
        self.assertTrue(checker.is_large_text("18pt", None))
        self.assertTrue(checker.is_large_text("14pt", "bold"))
        self.assertFalse(checker.is_large_text("14pt", None))
        self.assertFalse(checker.is_large_text("11pt", "bold"))

    def test_resolve_value_follows_var_chain(self):
        tokens = {"--a": "var(--b)", "--b": "#123456"}
        self.assertEqual(checker.resolve_value("var(--a)", tokens), "#123456")

    def test_is_anchor_selector_handles_descendant_and_compound_forms(self):
        # Real briefs style links through selectors like ".sub a", not just a
        # bare "a" -- the underline rule must recognize all of these as links.
        for selector in ("a", "a:hover", ".sub a", ".sub a:hover", "nav > a", "a.external"):
            with self.subTest(selector=selector):
                self.assertTrue(checker.is_anchor_selector(selector))
        for selector in (".emphasis", "abbr", ".data", "textarea"):
            with self.subTest(selector=selector):
                self.assertFalse(checker.is_anchor_selector(selector))

    def test_parse_length_to_px_supports_common_units(self):
        self.assertAlmostEqual(checker.parse_length_to_px("12pt"), 16.0, places=3)
        self.assertAlmostEqual(checker.parse_length_to_px("16px"), 16.0, places=3)
        self.assertAlmostEqual(checker.parse_length_to_px("1rem", root_px=16.0), 16.0, places=3)
        self.assertAlmostEqual(checker.parse_length_to_px("150%", root_px=16.0), 24.0, places=3)
        self.assertIsNone(checker.parse_length_to_px("2vw"))

    def test_computed_property_inline_style_wins_over_matching_rule(self):
        html = (
            '<html><body>'
            '<style>.x { color: red; background-color: #ffffff; }</style>'
            '<span class="x" style="background-color:#000000">t</span>'
            '</body></html>'
        )
        builder = checker.TreeBuilder()
        builder.feed(html)
        span = next(n for n in checker.walk(builder.root) if n.tag == "span")
        bg = checker.computed_property(span, [(".x", {"color": "red", "background-color": "#ffffff"})], {}, "background-color", "#ffffff")
        self.assertEqual(bg, "#000000")

    def test_main_exit_code_reflects_result(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(checker.main([str(TEMPLATE_PATH)]), 0)
            self.assertEqual(checker.main([str(FIXTURES_DIR / "bad-footer.html")]), 1)

    def test_main_exit_code_for_missing_file(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(checker.main([str(FIXTURES_DIR / "does-not-exist.html")]), 2)


if __name__ == "__main__":
    unittest.main()
