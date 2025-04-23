import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_with_headings(self):
        md = """# Heading 1

## Heading 2

This is a paragraph."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "## Heading 2",
                "This is a paragraph.",
            ],
        )
        
    def test_markdown_to_blocks_with_multiple_blank_lines(self):
        md = """First paragraph


Second paragraph


Third paragraph"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph",
                "Third paragraph",
            ],
        )
        
    def test_markdown_to_blocks_with_code_blocks(self):
        md = """Here is a code block:

```python
def hello_world():
    print("Hello, world!")
```

And here is another paragraph."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here is a code block:",
                "```python\ndef hello_world():\n    print(\"Hello, world!\")\n```",
                "And here is another paragraph.",
            ],
        )
        
    def test_markdown_to_blocks_with_lists(self):
        md = """Here's a list:

- Item 1
- Item 2
- Item 3

And here's another list:

1. First item
2. Second item
3. Third item"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here's a list:",
                "- Item 1\n- Item 2\n- Item 3",
                "And here's another list:",
                "1. First item\n2. Second item\n3. Third item",
            ],
        )
        
    def test_markdown_to_blocks_with_only_one_block(self):
        md = "This is a single paragraph without any blank lines."
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single paragraph without any blank lines.",
            ],
        )
        
    def test_markdown_to_blocks_with_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
    def test_markdown_to_blocks_with_only_whitespace(self):
        md = "    \n\n    \n    "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()