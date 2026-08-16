from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Base case 1 - Both trees empty - similar
    if not p and not q:
        return True

    # Base case 2 - either 1 of the trees are empty
    if not p or not q:
        return False

    # Base case 3 - val mismatch (building mismatch)
    if p.val != q.val:
        return False
    
    # 1. Explore left wings and right wings in tandem
    left_wing = isSameTree(p.left, q.left)
    right_wing = isSameTree(p.right, q.right)
    
    # 2. verify both wings are same
    return left_wing and right_wing
    
    