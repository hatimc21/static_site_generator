from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from markdown_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

def markdown_to_html_node(markdown):
    """
    Convert a markdown string to an HTML node.
    
    Args:
        markdown: A string containing markdown
        
    Returns:
        An HTMLNode representing the markdown document
    """
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Process each block and create HTML nodes
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = create_html_node_for_block(block, block_type)
        children.append(block_node)
    
    # Create a parent div node containing all the blocks
    return ParentNode("div", children)

def create_html_node_for_block(block, block_type):
    """
    Create an HTML node for a specific block based on its type.
    
    Args:
        block: A string containing a block of markdown
        block_type: The BlockType of the block
        
    Returns:
        An HTMLNode representing the block
    """
    if block_type == BlockType.PARAGRAPH:
        return create_paragraph_node(block)
    elif block_type == BlockType.HEADING:
        return create_heading_node(block)
    elif block_type == BlockType.CODE:
        return create_code_node(block)
    elif block_type == BlockType.QUOTE:
        return create_quote_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return create_unordered_list_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return create_ordered_list_node(block)
    else:
        raise ValueError(f"Unknown block type: {block_type}")

def text_to_children(text):
    """
    Convert a string of text with inline markdown to a list of HTMLNode objects.
    
    Args:
        text: A string containing inline markdown
        
    Returns:
        A list of HTMLNode objects representing the inline elements
    """
    # Convert text to TextNode objects
    text_nodes = text_to_textnodes(text)
    
    # Convert TextNode objects to HTMLNode objects
    return [text_node_to_html_node(node) for node in text_nodes]

def create_paragraph_node(block):
    """
    Create a paragraph HTML node.
    
    Args:
        block: A string containing a paragraph block
        
    Returns:
        A ParentNode with a 'p' tag
    """
    # Replace newlines with spaces in paragraphs
    paragraph_text = " ".join([line.strip() for line in block.split("\n")])
    children = text_to_children(paragraph_text)
    return ParentNode("p", children)

def create_heading_node(block):
    """
    Create a heading HTML node.
    
    Args:
        block: A string containing a heading block
        
    Returns:
        A ParentNode with an 'h1', 'h2', etc. tag
    """
    # Count the number of # at the beginning to determine heading level
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    
    # Extract the heading text (remove the # characters and leading space)
    heading_text = block[level:].strip()
    
    # Create the heading node
    children = text_to_children(heading_text)
    return ParentNode(f"h{level}", children)

def create_code_node(block):
    """
    Create a code block HTML node.
    
    Args:
        block: A string containing a code block
        
    Returns:
        A ParentNode with 'pre' and 'code' tags
    """
    # Remove the ``` markers from the beginning and end
    code_content = block[3:]
    if code_content.endswith("```"):
        code_content = code_content[:-3]
    
    # If there's a language specifier on the first line, remove it
    lines = code_content.split("\n")
    if len(lines) > 0 and lines[0].strip() and not lines[0].startswith("```"):
        # The first line might be a language specifier
        code_content = "\n".join(lines[1:])
    
    # Create a TextNode for the code content (no inline parsing)
    text_node = TextNode(code_content.strip(), TextType.TEXT)
    code_leaf = text_node_to_html_node(text_node)
    
    # Wrap in a code tag and then a pre tag
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])

def create_quote_node(block):
    """
    Create a blockquote HTML node.
    
    Args:
        block: A string containing a quote block
        
    Returns:
        A ParentNode with a 'blockquote' tag
    """
    # Remove the > prefix from each line
    lines = block.split("\n")
    cleaned_lines = [line[1:].strip() for line in lines]
    quote_content = " ".join(cleaned_lines)
    
    # Create the quote node
    children = text_to_children(quote_content)
    return ParentNode("blockquote", children)

def create_unordered_list_node(block):
    """
    Create an unordered list HTML node.
    
    Args:
        block: A string containing an unordered list block
        
    Returns:
        A ParentNode with a 'ul' tag containing 'li' children
    """
    # Split into list items
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Remove the '- ' prefix from each line
        item_text = line[2:].strip()
        item_children = text_to_children(item_text)
        list_items.append(ParentNode("li", item_children))
    
    return ParentNode("ul", list_items)

def create_ordered_list_node(block):
    """
    Create an ordered list HTML node.
    
    Args:
        block: A string containing an ordered list block
        
    Returns:
        A ParentNode with an 'ol' tag containing 'li' children
    """
    # Split into list items
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Find the position after the number and period
        period_pos = line.find('.')
        if period_pos != -1:
            # Extract the item text (skip number, period, and space)
            item_text = line[period_pos + 1:].strip()
            item_children = text_to_children(item_text)
            list_items.append(ParentNode("li", item_children))
    
    return ParentNode("ol", list_items)