'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def sum_rec(node, sum, result, results):
            if node is None:
                if sum == 0:
                    results.append(result)
            else:
                sum -= node.val
                result = result + [node.val]  # cannot use +=
                if node.left is None:
                    sum_rec(node.right, sum, result, results)
                elif node.right is None:
                    sum_rec(node.left, sum, result, results)
                else:
                    sum_rec(node.left, sum, result, results)
                    sum_rec(node.right, sum, result, results)
        result = []
        results = []
        sum_rec(root, sum, result, results)
        return results if root else []
