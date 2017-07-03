'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth_rec(node):
            if node is None:
                return 0

            left = depth_rec(node.left)
            right = depth_rec(node.right)
            if abs(left - right) > 1:
                raise Exception('unblanced')
            else:
                return max(left, right) + 1
        try:
            depth_rec(root)
        except:
            return False
        return True
