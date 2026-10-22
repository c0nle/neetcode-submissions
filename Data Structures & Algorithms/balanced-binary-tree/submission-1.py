# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        diff = 0
        
        def dfs(root):
            nonlocal diff
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            diff = max(abs(left - right),diff)

            return 1 + max(left,right)
        
        dfs(root)

        return True if diff <= 1 else False


            