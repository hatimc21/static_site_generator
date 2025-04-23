import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")
        
    def test_title_with_spaces(self):
        markdown = "#   Title with spaces   "
        self.assertEqual(extract_title(markdown), "Title with spaces")
        
    def test_title_with_formatting(self):
        markdown = "# Title with **bold** and _italic_"
        self.assertEqual(extract_title(markdown), "Title with **bold** and _italic_")
        
    def test_title_after_content(self):
        markdown = "Some content before the title\n\n# The Real Title\n\nMore content"
        self.assertEqual(extract_title(markdown), "The Real Title")
        
    def test_title_with_multiple_headers(self):
        markdown = "# Main Title\n\n## Secondary Title"
        self.assertEqual(extract_title(markdown), "Main Title")
        
    def test_no_title(self):
        markdown = "This markdown has no title"
        with self.assertRaises(ValueError):
            extract_title(markdown)
        
    def test_only_secondary_headers(self):
        markdown = "## Secondary Title\n\n### Tertiary Title"
        with self.assertRaises(ValueError):
            extract_title(markdown)
        
    def test_title_with_symbols(self):
        markdown = "# Title with symbols: !@#$%^&*()"
        self.assertEqual(extract_title(markdown), "Title with symbols: !@#$%^&*()")
        
    def test_empty_string(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()