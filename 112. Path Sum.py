'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def sum_rec(node, sum):
            if node is None:
                return sum == 0
            sum -= node.val
            if node.left is None:
                return sum_rec(node.right, sum)
            elif node.right is None:
                return sum_rec(node.left, sum)
            else:
                return sum_rec(node.left, sum) or sum_rec(node.right, sum)
        return sum_rec(root, sum) if root else False
