# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(roota,rootb):
            if not roota and not rootb :
                return True
            elif not roota or not rootb:
                return False
            
            if roota.val == rootb.val:
                return dfs(roota.left,rootb.left) and dfs(roota.right,rootb.right)
            else:
                return False
        return dfs(p,q)