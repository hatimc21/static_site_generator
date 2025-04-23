import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )
        
    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3 with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3 with <b>bold</b></h3></div>",
        )
        
    def test_blockquote(self):
        md = """
> This is a blockquote
> with multiple lines
> and **formatting**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote with multiple lines and <b>formatting</b></blockquote></div>",
        )
        
    def test_unordered_list(self):
        md = """
- Item 1
- Item 2 with **bold**
- Item 3 with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b></li><li>Item 3 with <code>code</code></li></ul></div>",
        )
        
    def test_ordered_list(self):
        md = """
1. First item
2. Second item with _italic_
3. Third item with [link](https://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <i>italic</i></li><li>Third item with <a href=\"https://example.com\">link</a></li></ol></div>",
        )
        
    def test_codeblock_with_language(self):
        md = """
```python
def hello():
    print("Hello, world!")
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def hello():\n    print(\"Hello, world!\")</code></pre></div>",
        )
        
    def test_mixed_content(self):
        md = """
# Document Title

This is a paragraph with **bold** and _italic_ text.

## Subsection

- List item 1
- List item 2

```
Some code
```

> A quote with **formatting**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Document Title</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Subsection</h2><ul><li>List item 1</li><li>List item 2</li></ul><pre><code>Some code</code></pre><blockquote>A quote with <b>formatting</b></blockquote></div>",
        )
        
    def test_empty_document(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")
        
    def test_paragraph_with_links_and_images(self):
        md = """
This is a paragraph with a [link](https://example.com) and an ![image](https://example.com/image.jpg).
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with a <a href=\"https://example.com\">link</a> and an <img src=\"https://example.com/image.jpg\" alt=\"image\"></img>.</p></div>",
        )


if __name__ == "__main__":
    unittest.main()