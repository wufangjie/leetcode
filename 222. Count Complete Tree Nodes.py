# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lh = self.get_depth(root.left)
        rh = self.get_depth(root.right)
        if lh == rh:
            return 2 ** lh + self.countNodes(root.right)
        else:
            return 2 ** rh + self.countNodes(root.left)

    @staticmethod
    def get_depth(node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth
