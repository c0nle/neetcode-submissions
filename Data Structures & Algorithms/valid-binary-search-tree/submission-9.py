# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

            res = True

            def dfs(node,leftMin,rightMax):
                nonlocal res
                if not node:
                    return
                if node.left:
                    if not (node.left.val < node.val and node.left.val < leftMin and node.left.val > rightMax):
                        res = False
                        return
                    dfs(node.left,node.val,rightMax)
                if node.right:
                    if not (node.right.val > node.val and node.right.val > rightMax and node.right.val < leftMin):
                        res = False
                        return
                    dfs(node.right,leftMin,node.val) 
            
            dfs(root,float("inf"),float("-inf"))

            return res
                    
                
                
