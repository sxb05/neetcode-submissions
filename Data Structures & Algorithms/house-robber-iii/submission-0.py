# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0]

            lp = dfs(root.left)
            rp = dfs(root.right)


            withroot = root.val + lp[1] + rp[1]
            woutroot = max(lp) + max(rp)



            return [withroot,woutroot]
        return  max(dfs(root))
        