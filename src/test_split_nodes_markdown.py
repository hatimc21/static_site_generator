import unittest

from textnode import TextNode, TextType
from split_nodes_markdown import split_nodes_image, split_nodes_link


class TestSplitNodesMarkdown(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) at the start",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the start", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_image_at_end(self):
        node = TextNode(
            "At the end is an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("At the end is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
        
    def test_split_image_only(self):
        node = TextNode(
            "![standalone image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("standalone image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
        
    def test_split_image_none(self):
        node = TextNode(
            "This text has no images at all",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text has no images at all", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_image_multiple_nodes(self):
        node1 = TextNode(
            "First text with ![image1](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "Second text with ![image2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("First text with ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("Second text with ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
        
    def test_split_image_non_text_nodes(self):
        node1 = TextNode(
            "Text with ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "Bold text",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("Bold text", TextType.BOLD),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
        
    def test_split_link_at_start(self):
        node = TextNode(
            "[link](https://www.example.com) at the start",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" at the start", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_link_at_end(self):
        node = TextNode(
            "At the end is a [link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("At the end is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )
        
    def test_split_link_only(self):
        node = TextNode(
            "[standalone link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("standalone link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )
        
    def test_split_link_none(self):
        node = TextNode(
            "This text has no links at all",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has no links at all", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_link_multiple_nodes(self):
        node1 = TextNode(
            "First text with [link1](https://www.example1.com)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "Second text with [link2](https://www.example2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("First text with ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://www.example1.com"),
                TextNode("Second text with ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://www.example2.com"),
            ],
            new_nodes,
        )
        
    def test_split_link_non_text_nodes(self):
        node1 = TextNode(
            "Text with [link](https://www.example.com)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "Bold text",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode("Bold text", TextType.BOLD),
            ],
            new_nodes,
        )
        
    def test_split_link_with_images(self):
        node = TextNode(
            "Text with ![image](https://example.com/image.png) and [link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text with ![image](https://example.com/image.png) and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )
        
    def test_split_image_with_links(self):
        node = TextNode(
            "Text with [link](https://www.example.com) and ![image](https://example.com/image.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text with [link](https://www.example.com) and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()