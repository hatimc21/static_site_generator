def markdown_to_blocks(markdown):
    """
    Split a markdown string into blocks based on blank lines.
    
    Args:
        markdown: A string containing markdown text
        
    Returns:
        A list of strings, each representing a block of markdown
    """
    # Split the markdown by double newlines to separate blocks
    blocks = markdown.split("\n\n")
    
    # Process each block: strip whitespace and filter out empty blocks
    result = []
    for block in blocks:
        # Strip leading and trailing whitespace
        cleaned_block = block.strip()
        
        # Only include non-empty blocks
        if cleaned_block:
            result.append(cleaned_block)
            
    return result