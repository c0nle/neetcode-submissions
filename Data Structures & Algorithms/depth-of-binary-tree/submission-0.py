# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        right,left = 1,1

        if curr is None:
            return 0
        if curr.left is not None:
            left = 1 + self.maxDepth(curr.left)
        if curr.right is not None:
            right = 1 + self.maxDepth(curr.right)
        
        return max(left,right)
