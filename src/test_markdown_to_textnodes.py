import unittest

from textnode import TextNode, TextType
from markdown_to_textnodes import text_to_textnodes


class TestMarkdownToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_simple(self):
        text = "This is **text** with an _italic_ word and a `code block`."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_comprehensive(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )
        
    def test_text_to_textnodes_plain_text(self):
        text = "This is just plain text without any special formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("This is just plain text without any special formatting.", TextType.TEXT)],
            nodes,
        )
        
    def test_text_to_textnodes_only_bold(self):
        text = "**Bold text only**"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Bold text only", TextType.BOLD)],
            nodes,
        )
        
    def test_text_to_textnodes_only_italic(self):
        text = "_Italic text only_"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Italic text only", TextType.ITALIC)],
            nodes,
        )
        
    def test_text_to_textnodes_only_code(self):
        text = "`Code text only`"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Code text only", TextType.CODE)],
            nodes,
        )
        
    def test_text_to_textnodes_only_image(self):
        text = "![Image alt text](https://example.com/image.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Image alt text", TextType.IMAGE, "https://example.com/image.png")],
            nodes,
        )
        
    def test_text_to_textnodes_only_link(self):
        text = "[Link text](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Link text", TextType.LINK, "https://example.com")],
            nodes,
        )
        
    def test_text_to_textnodes_adjacent_elements(self):
        text = "**Bold**_Italic_`Code`![Image](https://example.com/image.png)[Link](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Bold", TextType.BOLD),
                TextNode("Italic", TextType.ITALIC),
                TextNode("Code", TextType.CODE),
                TextNode("Image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode("Link", TextType.LINK, "https://example.com"),
            ],
            nodes,
        )
        
    def test_text_to_textnodes_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("", TextType.TEXT)],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()