'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Q = deque()
        Q.append((0, root))
        results = [[]]
        reached_level = 0
        while Q:
            level, node = Q.popleft()
            if level > reached_level:
                results.append([])
                reached_level += 1
            results[level].append(node.val)
            if node.left:
                Q.append((level + 1, node.left))
            if node.right:
                Q.append((level + 1, node.right))
        return results
