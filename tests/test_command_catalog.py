import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from prompt_builder import load_commands, build_prompt


class CommandCatalogTest(unittest.TestCase):
    def test_exactly_100_unique_commands(self):
        catalog = load_commands()
        self.assertEqual(len(catalog), 100)
        self.assertEqual(len({c['category'] for c in catalog.values()}), 10)
        self.assertEqual({c['kind'] for c in catalog.values()}, {'visual','modifier','workflow'})

    def test_required_original_commands(self):
        catalog = load_commands()
        for command in ['/cleanflyer','/herooffer-minimal','/pixel-lock','/auto-gallery','/marketplace-pro','/listing-audit']:
            self.assertIn(command,catalog)
        self.assertTrue(catalog['/cleanflyer']['must_be_text_free'])
        self.assertFalse(catalog['/herooffer-minimal']['for_cover_by_default'])
        self.assertTrue(catalog['/herooffer-minimal']['verified_claims_required'])

    def test_prompt_has_user_schema(self):
        prompt = build_prompt('/herooffer-minimal','Mouse Attack Shark X11','Black','Mouse super leve','63g','img.png','/pixel-lock,/quality-check')
        for part in ['Product: Mouse Attack Shark X11','Color: Black','Theme1: Mouse super leve','Theme2: 63g','Image: img.png','Options: /pixel-lock, /quality-check']:
            self.assertIn(part,prompt)

    def test_invalid_commands_rejected(self):
        with self.assertRaises(ValueError):
            build_prompt('/fake','Mouse')
        with self.assertRaises(ValueError):
            build_prompt('/cleanflyer','Mouse',options='/imaginary')
        with self.assertRaises(ValueError):
            build_prompt('/cleanflyer','')

    def test_every_command_documented(self):
        doc = (ROOT/'skills/marketplace-pro/references/catalogo-100-comandos.md').read_text(encoding='utf-8')
        for command in load_commands():
            self.assertIn('`'+command+'`',doc)

    def test_no_hard_requirement_on_img_reference_at_prompt_build(self):
        text = build_prompt('/title-pro','Tênis casual')
        self.assertIn('Product: Tênis casual',text)
        self.assertNotIn('Image:',text)

if __name__ == '__main__':
    unittest.main()
