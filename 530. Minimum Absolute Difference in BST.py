# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils import TreeNode


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre, theMin = float('-inf'), float('inf')

        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            theMin = min(theMin, node.val - pre)
            pre = node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return theMin


print(Solution().getMinimumDifference(TreeNode(1, None, TreeNode(3, TreeNode(2)))))
