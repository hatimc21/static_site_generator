import unittest
from enum import Enum

from textnode import TextNode, TextType
from htmlnode import LeafNode
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertIsInstance(html_node, LeafNode)
    
    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertIsInstance(html_node, LeafNode)
    
    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertIsInstance(html_node, LeafNode)
    
    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertIsInstance(html_node, LeafNode)
        
    def test_link(self):
        node = TextNode("Click me", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})
        self.assertIsInstance(html_node, LeafNode)
        
    def test_image(self):
        node = TextNode("Alt text for image", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Alt text for image"})
        self.assertIsInstance(html_node, LeafNode)
        
    def test_invalid_type(self):
        # Create a mock TextNode with an invalid TextType
        class MockTextType(Enum):
            INVALID = "invalid"
            
        node = TextNode("Invalid node", MockTextType.INVALID)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
            
    def test_html_generation(self):
        # Test that the generated HTML nodes correctly render to HTML
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")
        
        node = TextNode("Click me", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Click me</a>')
        
        node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="image.jpg" alt="Alt text"></img>')


if __name__ == "__main__":
    unittest.main()