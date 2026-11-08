import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from quality_check import validate_listing  # noqa: E402


class QualityCheckTests(unittest.TestCase):
    def setUp(self):
        self.good = {
            "title": "Headset marca Exemplo modelo H1 preto com fio",
            "description": "Headset modelo H1 da marca Exemplo, com fio e cor preta. Confira as informações, especificações e a compatibilidade antes de comprar.",
            "brand": "Exemplo",
            "model": "H1",
            "attributes": {"cor": "preto"},
            "images": [{"role": "cover", "width": 1200, "height": 1200, "contains_overlay": False, "ai_generated": False}],
        }

    def test_baseline_has_no_warnings(self):
        self.assertEqual(validate_listing(self.good), [])

    def test_category_title_limit_is_configurable(self):
        findings = validate_listing(self.good, title_limit=15)
        self.assertTrue(any(i["field"] == "title" and i["priority"] == "P1" for i in findings))

    def test_unverified_ai_image_is_priority_zero(self):
        bad = dict(self.good)
        bad["images"] = [{"role": "cover", "ai_generated": True}]
        self.assertTrue(any(i["priority"] == "P0" for i in validate_listing(bad)))

    def test_promotional_term(self):
        bad = dict(self.good)
        bad["title"] = "PROMOÇÃO Headset Exemplo H1"
        findings = validate_listing(bad)
        self.assertTrue(any("promoção" in i["message"] for i in findings))


if __name__ == "__main__":
    unittest.main()
