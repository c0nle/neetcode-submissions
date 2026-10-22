# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root,subRoot):
            if not root and not subRoot:
                return True
            if (not root or not subRoot) and (root or subRoot) or root.val != subRoot.val:
                return False
            
            return sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right)

        res = False

        def dfs(root):
            nonlocal res
            if not root:
                return
            
            res = res or sameTree(root,subRoot)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return res
        