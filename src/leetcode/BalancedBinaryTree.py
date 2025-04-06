from typing import Optional
from TreeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return abs(left_height-right_height) <=1 and  self.isBalanced(root.left) and self.isBalanced(root.right)    

    def height(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0;
        return 1 + max(self.height(root.left), self.height(root.right))
