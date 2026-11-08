from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'marketplace-pro'

class VisualCommandTests(unittest.TestCase):
    def test_comandos_exist(self):
        doc = (SKILL / 'references' / 'comandos-visuais.md').read_text(encoding='utf-8')
        self.assertIn('`/cleanflyer`', doc)
        self.assertIn('`/herooffer-minimal`', doc)
        self.assertIn('No text, no graphic icons', doc)
        self.assertIn('Brazilian Portuguese', doc)
    def test_skill_references_visual_commands(self):
        main = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/comandos-visuais.md', main)
    def test_banner_cannot_be_marked_as_cover(self):
        doc = (SKILL / 'references' / 'comandos-visuais.md').read_text(encoding='utf-8')
        self.assertIn('não marcar como pronto para usar no anúncio', doc)
        self.assertIn('não usar como capa', doc)
    def test_project_has_shortcuts(self):
        project = (ROOT / 'chatgpt' / 'INSTRUCOES_PROJETO.md').read_text(encoding='utf-8')
        self.assertIn('/cleanflyer', project)
        self.assertIn('/herooffer-minimal', project)

if __name__ == '__main__':
    unittest.main()
