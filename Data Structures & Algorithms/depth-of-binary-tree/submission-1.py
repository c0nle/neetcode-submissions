# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root,res):
            if not root:
                return res
            
            res += 1
            
            return max(dfs(root.right,res),dfs(root.left,res))
        
        return dfs(root,0)