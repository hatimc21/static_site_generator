from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    """
    Split TextNode objects based on markdown images.
    
    Args:
        old_nodes: A list of TextNode objects.
        
    Returns:
        A new list of TextNode objects where any TEXT nodes containing images
        are split into TEXT and IMAGE nodes.
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # Only process TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Extract images from the text
        text = old_node.text
        image_matches = extract_markdown_images(text)
        
        # If no images, keep the node as is
        if len(image_matches) == 0:
            new_nodes.append(old_node)
            continue
            
        # Process the text and add nodes
        remaining_text = text
        last_end = 0
        
        for alt_text, url in image_matches:
            # Find the full image markdown
            image_md = f"![{alt_text}]({url})"
            start_index = remaining_text.find(image_md, last_end)
            
            if start_index == -1:
                continue
                
            # Add text before the image
            if start_index > last_end:
                new_nodes.append(TextNode(remaining_text[last_end:start_index], TextType.TEXT))
                
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Update the last ending position
            last_end = start_index + len(image_md)
        
        # Add any remaining text
        if last_end < len(remaining_text):
            new_nodes.append(TextNode(remaining_text[last_end:], TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Split TextNode objects based on markdown links.
    
    Args:
        old_nodes: A list of TextNode objects.
        
    Returns:
        A new list of TextNode objects where any TEXT nodes containing links
        are split into TEXT and LINK nodes.
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # Only process TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Extract links from the text
        text = old_node.text
        link_matches = extract_markdown_links(text)
        
        # If no links, keep the node as is
        if len(link_matches) == 0:
            new_nodes.append(old_node)
            continue
            
        # Process the text and add nodes
        remaining_text = text
        last_end = 0
        
        for anchor_text, url in link_matches:
            # Find the full link markdown
            link_md = f"[{anchor_text}]({url})"
            start_index = remaining_text.find(link_md, last_end)
            
            if start_index == -1:
                continue
                
            # Add text before the link
            if start_index > last_end:
                new_nodes.append(TextNode(remaining_text[last_end:start_index], TextType.TEXT))
                
            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            # Update the last ending position
            last_end = start_index + len(link_md)
        
        # Add any remaining text
        if last_end < len(remaining_text):
            new_nodes.append(TextNode(remaining_text[last_end:], TextType.TEXT))
    
    return new_nodes