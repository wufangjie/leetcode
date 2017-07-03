# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        while stack:
            current = stack.pop()
            if k == 0:
                return current.val
            k -= 1
            node = current.right
            while node:
                stack.append(node)
                node = node.left
