import re

def extract_title(markdown):
    """
    Extract the h1 header (title) from a markdown string.
    
    Args:
        markdown: A string containing markdown text
        
    Returns:
        The title string (without the # and any leading/trailing whitespace)
        
    Raises:
        ValueError: If no h1 header is found
    """
    # Look for a line that starts with a single # followed by a space
    lines = markdown.split("\n")
    for line in lines:
        match = re.match(r"^# (.+)$", line.strip())
        if match:
            return match.group(1).strip()
    
    # If we didn't find an h1 header, raise an exception
    raise ValueError("No h1 header found in the markdown content")