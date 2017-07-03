'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth_rec(node):
            if node is None:
                return 0
            left, right = depth_rec(node.left), depth_rec(node.right)
            return (min(left, right) if left * right else max(left, right)) + 1
        return depth_rec(root)
