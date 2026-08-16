def isSymmetric(root: Optional[TreeNode]) -> bool:
    # Base case - empty tree = perfectly symmetrical
    if not root:
        return True
    
    # Else, begin left & right scan using helper fn
    return isMirror(root.left, root.right)

def isMirror(l_node: Optional[TreeNode], r_node: Optional[TreeNode]) -> bool:
    # inner base case 1 - both node empty = symmetric
    if not l_node and not r_node:
        return True

    # inner base case 2 - either node empty = asymmetric
    if not l_node or not r_node:
        return False

    # inner base case 3 - both node exist but value differ
    if l_node.val != r_node.val:
        return False
    
    # 1. Begin exploration of inner & outer wing (symmetric traversal)
    inner_wing_symmetric = isMirror(l_node.right, r_node.left)
    outer_wing_symmetric = isMirror(l_node.left, r_node.right)
    
    # 2. Ensure both wings are symmetric
    return inner_wing_symmetric and outer_wing_symmetric

    

    