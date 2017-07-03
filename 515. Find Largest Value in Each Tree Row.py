from utils import TreeNode
from collections import deque


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        level = object()
        Q = deque([root, level])
        result = []
        while True:
            theMax = float('-inf')
            while True:
                node = Q.popleft()
                if node is level:
                    result.append(theMax)
                    if Q:
                        Q.append(level)
                        break
                    else:
                        return result
                theMax = max(theMax, node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
