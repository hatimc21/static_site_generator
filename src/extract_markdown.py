import re

def extract_markdown_images(text):
    """
    Extract markdown images from the given text.
    Returns a list of tuples containing (alt_text, url).
    
    Example:
    "This is text with a ![image](https://example.com/image.png)"
    Returns: [("image", "https://example.com/image.png")]
    """
    # The regex pattern matches:
    # - ![alt text](url)
    # - Capturing groups for the alt text and URL
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Extract markdown links from the given text.
    Returns a list of tuples containing (anchor_text, url).
    
    Example:
    "This is text with a [link](https://example.com)"
    Returns: [("link", "https://example.com")]
    """
    # The regex pattern matches:
    # - [anchor text](url)
    # - But not ![alt text](url) which is an image
    # - Capturing groups for the anchor text and URL
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches