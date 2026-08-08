import unittest
import os
from scripts.validate_links import parse_readme_links, validate_link_format

class TestResourceLinks(unittest.TestCase):
    def test_parse_readme_links(self):
        readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
        links = parse_readme_links(readme_path)
        self.assertGreater(len(links), 0)

    def test_link_format(self):
        self.assertTrue(validate_link_format("https://bioconductor.org/packages/DESeq2/"))
        self.assertFalse(validate_link_format("ftp://invalid.link"))

if __name__ == '__main__':
    unittest.main()
