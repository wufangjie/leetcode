# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = {}
        Q = deque([root, None])
        level = 0
        while Q:
            node = Q.popleft()
            if node:
                result[level] = node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            elif Q:
                Q.append(None)
                level += 1
        return [result[l] for l in range(level+1)]

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
Solution().rightSideView(root)
