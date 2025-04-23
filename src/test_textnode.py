import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        self.assertEqual(node, node2)
    
    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_different_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.different.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_with_none_url(self):
        node = TextNode("This is a text", TextType.TEXT)
        node2 = TextNode("This is a text", TextType.TEXT, None)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        self.assertEqual(
            repr(node),
            "TextNode(This is a link, link, https://www.example.com)"
        )
    
    def test_repr_with_none_url(self):
        node = TextNode("This is text", TextType.TEXT)
        self.assertEqual(
            repr(node),
            "TextNode(This is text, text, None)"
        )


if __name__ == "__main__":
    unittest.main()