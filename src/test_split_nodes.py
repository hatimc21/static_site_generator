import unittest
from enum import Enum

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))
        
    def test_split_with_bold(self):
        node = TextNode("This is text with a **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold word", TextType.BOLD))
        
    def test_split_with_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" text", TextType.TEXT))
        
    def test_multiple_delimiters(self):
        node = TextNode("This `code` has `multiple` delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("This ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" has ", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("multiple", TextType.CODE))
        self.assertEqual(new_nodes[4], TextNode(" delimiters", TextType.TEXT))
        
    def test_no_delimiters(self):
        node = TextNode("This text has no delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This text has no delimiters", TextType.TEXT))
        
    def test_only_opening_delimiter(self):
        node = TextNode("This text has only an opening ` delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This text has only an opening ` delimiter", TextType.TEXT))
        
    def test_empty_content_between_delimiters(self):
        node = TextNode("Empty ``", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("Empty ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("", TextType.CODE))
        
    def test_adjacent_delimiters(self):
        node = TextNode("Adjacent **bold**_italic_", TextType.TEXT)
        # First split for bold
        intermediate_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Then split for italic
        new_nodes = split_nodes_delimiter(intermediate_nodes, "_", TextType.ITALIC)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Adjacent ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("italic", TextType.ITALIC))
        
    def test_multiple_input_nodes(self):
        node1 = TextNode("First `code`", TextType.TEXT)
        node2 = TextNode("Second **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        
        # For debugging
        print("\nTest multiple input nodes results:")
        for i, node in enumerate(new_nodes):
            print(f"Node {i}: {node}")
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("First ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode("Second **bold**", TextType.TEXT))
        
    def test_non_text_nodes_unchanged(self):
        node1 = TextNode("Text `code`", TextType.TEXT)
        node2 = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Text ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode("Already bold", TextType.BOLD))
        
    def test_delimiter_at_start(self):
        node = TextNode("`code` at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[1], TextNode(" at start", TextType.TEXT))
        
    def test_delimiter_at_end(self):
        node = TextNode("at end `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("at end ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))


if __name__ == "__main__":
    unittest.main()