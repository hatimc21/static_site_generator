import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with no props
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single prop
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://www.example.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={
                "href": "https://www.example.com",
                "target": "_blank",
                "class": "link-button"
            }
        )
        # Since dictionaries don't guarantee order, we'll check for each attribute separately
        props_html = node.props_to_html()
        self.assertIn(' href="https://www.example.com"', props_html)
        self.assertIn(' target="_blank"', props_html)
        self.assertIn(' class="link-button"', props_html)
        
    def test_repr(self):
        # Test the representation of the HTMLNode
        node = HTMLNode(
            tag="p",
            value="Hello, world!",
            props={"class": "paragraph"}
        )
        expected = 'HTMLNode(tag=p, value=Hello, world!, children=None, props={\'class\': \'paragraph\'})'
        self.assertEqual(repr(node), expected)
        
    def test_none_values(self):
        # Test with all None values
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_to_html_raises_error(self):
        # Test that to_html raises NotImplementedError
        node = HTMLNode(tag="p", value="Hello, world!")
        with self.assertRaises(NotImplementedError):
            node.to_html()


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
        
    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Bold text")
        self.assertEqual(node.to_html(), "<strong>Bold text</strong>")
        
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Image description", {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="An image">Image description</img>')
        
    def test_leaf_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        child4 = LeafNode(None, "Normal text")
        parent_node = ParentNode("p", [child1, child2, child3, child4])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )
        
    def test_to_html_with_nested_parent_nodes(self):
        leaf1 = LeafNode("span", "Text 1")
        leaf2 = LeafNode("span", "Text 2")
        inner_parent1 = ParentNode("div", [leaf1])
        inner_parent2 = ParentNode("div", [leaf2])
        outer_parent = ParentNode("section", [inner_parent1, inner_parent2])
        self.assertEqual(
            outer_parent.to_html(),
            "<section><div><span>Text 1</span></div><div><span>Text 2</span></div></section>"
        )
        
    def test_to_html_complex_nesting(self):
        text1 = LeafNode(None, "Hello, ")
        bold = LeafNode("b", "world")
        text2 = LeafNode(None, "!")
        em = LeafNode("em", "Emphasis")
        inner_div = ParentNode("div", [text1, bold, text2])
        article = ParentNode("article", [inner_div, em])
        self.assertEqual(
            article.to_html(),
            "<article><div>Hello, <b>world</b>!</div><em>Emphasis</em></article>"
        )
        
    def test_to_html_empty_children_list(self):
        # An empty list of children is valid - it just creates a tag with no content
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")
        
    def test_no_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")]).to_html()
            
    def test_no_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()


if __name__ == "__main__":
    unittest.main()