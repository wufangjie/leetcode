# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode
from collections import deque


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Q = deque([(1, root), (0, None)])
        theMax = 1
        start = end = -1
        while Q:
            pos, node = Q.popleft()
            if node is None:
                theMax = max(theMax, end - start + 1)
                start = end = -1
                if Q:
                    Q.append((0, None))
            else:
                if start == -1:
                    start = pos
                else:
                    end = pos
                pos <<= 1
                if node.left:
                    Q.append((pos - 1, node.left))
                if node.right:
                    Q.append((pos, node.right))
        return theMax

# root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)),
#                 TreeNode(2, None, TreeNode(9)))

root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))),
                TreeNode(2, None, TreeNode(9, None, TreeNode(7))))

print(Solution().widthOfBinaryTree(root))
