# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # If the main tree is empty, it cannot contain a subRoot
        if not root:
            return False
        
        # Check if the trees match starting from the current node
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, search in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both are empty trees
        if not p and not q:
            return True
        # One is empty and the other is not, or values do not match
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right structures
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        