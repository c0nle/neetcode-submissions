# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif self.equal(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
    def equal(self,roota,rootb) -> bool:
        def dfs(roota,rootb):
            if not roota and not rootb:
                return True
            elif not roota or not rootb:
                return False

            return roota.val == rootb.val and dfs(roota.left,rootb.left) and dfs(roota.right,rootb.right)
        return dfs(roota,rootb)