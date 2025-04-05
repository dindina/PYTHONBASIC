# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def random_tree() -> Optional['TreeNode']:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        return root
            
    
    @staticmethod
    def build_tree(nodes: list[Optional[int]]) -> Optional['TreeNode']:
        if not nodes:
            return None

        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            current_node = queue.pop(0)

            left_val = nodes[i] if i < len(nodes) else None
            i += 1
            if left_val is not None:
                current_node.left = TreeNode(left_val)
                queue.append(current_node.left)

            right_val = nodes[i] if i < len(nodes) else None
            i += 1
            if right_val is not None:
                current_node.right = TreeNode(right_val)
                queue.append(current_node.right)

        return root

    @staticmethod
    def print_tree(root: Optional['TreeNode']):
        
        def inorder_print(node, level=0):
            if node:
                inorder_print(node.right, level + 1)
                print("  " * level + str(node.val))
                inorder_print(node.left, level + 1)
        inorder_print(root)

    # Example usage:
nodes = [4, 2, 7, 1, 3, None, 9]
root = TreeNode.build_tree(nodes)  # Called on the class itself
TreeNode.print_tree(root)  # Called on the class itself


print("random tree")
TreeNode.print_tree(TreeNode.random_tree())

            