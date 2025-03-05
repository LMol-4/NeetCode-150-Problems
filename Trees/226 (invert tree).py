# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            if current:
                queue.append(current.left)
                queue.append(current.right)
                temp = current.left
                current.left = current.right
                current.right = temp

        return root