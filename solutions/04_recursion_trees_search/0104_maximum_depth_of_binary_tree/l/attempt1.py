from typing import Optional

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root: Optional[TreeNode]) -> int:
    # 1. Base case check - Empty desk - no depth
    if not root:
        return 0
    
    # 2. CEO delegate to left & right VP
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)
    
    # 3. Evaluate results from left & right VP and add 1 to max of both 
    return 1 + max(left_height, right_height)