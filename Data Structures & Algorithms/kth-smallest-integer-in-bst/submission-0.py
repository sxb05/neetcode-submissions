# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr = root
        ar=[]
        def dfs(cur):
            if not cur:
                return

            dfs(cur.left)
            ar.append(cur.val)
            dfs(cur.right)

        dfs(curr)
        return ar[k - 1]

        