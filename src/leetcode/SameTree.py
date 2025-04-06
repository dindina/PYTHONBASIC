from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False                
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

tree1 = TreeNode.random_tree()
tree2 = TreeNode.random_tree()
sol = Solution()
print(sol.isSameTree(tree1,tree2))

tree1 = TreeNode.random_tree1()
tree2 = TreeNode.random_tree()
print(sol.isSameTree(tree1,tree2))