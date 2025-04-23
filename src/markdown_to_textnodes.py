from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter
from split_nodes_markdown import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    """
    Convert markdown text to a list of TextNode objects.
    
    Args:
        text: Raw markdown text string
        
    Returns:
        A list of TextNode objects representing the markdown elements
    """
    # Start with a single text node containing the entire text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split by markdown delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Split by markdown images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes