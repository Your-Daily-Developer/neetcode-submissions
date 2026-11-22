from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Empty subRoot is always a subtree
        if not subRoot:
            return True
        # Non-empty subRoot cannot be a subtree of an empty tree
        if not root:
            return False
        
        # Check if the trees rooted at the current nodes are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise keep searching in left and right subtrees
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty → identical
        if not p and not q:
            return True
        # One empty, one not → different
        if not p or not q:
            return False
        # Values differ → different
        if p.val != q.val:
            return False
        
        # Recursively check left and right children
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))