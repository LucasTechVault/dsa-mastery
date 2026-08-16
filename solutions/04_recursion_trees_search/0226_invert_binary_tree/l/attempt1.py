from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Base case - empty node - no inversion needed
    if not root:
        return
    
    # 1. Perform swap of direct reports
    root.left, root.right = root.right, root.left
    
    # 2. Ask reports to invert their reports
    invertTree(root.left)
    invertTree(root.right)
    
    # 3. return the node that already performed the inversion
    return root