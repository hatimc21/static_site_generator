from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    """
    Determine the type of a markdown block.
    
    Args:
        block: A string containing a block of markdown
        
    Returns:
        A BlockType enum value representing the type of the block
    """
    # Check for heading (starts with 1-6 # characters followed by a space)
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Check for code block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote block (each line starts with >)
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list (each line starts with "- ")
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list (lines start with 1. 2. 3. etc.)
    if _is_ordered_list(lines):
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH

def _is_ordered_list(lines):
    """
    Check if the given lines form an ordered list.
    
    An ordered list must have each line start with a number followed by a period and space,
    and the numbers must start at 1 and increment by 1 for each line.
    """
    if not lines:
        return False
        
    for i, line in enumerate(lines, 1):
        expected_prefix = f"{i}. "
        if not line.startswith(expected_prefix):
            return False
            
    return True