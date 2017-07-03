from utils import TreeNode
from collections import deque


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = object()
        Q = deque([root, level])
        first = root.val
        while Q:
            node = Q.popleft()
            if node is level:
                if Q:
                    first = Q[0].val
                    Q.append(level)
                else:
                    return first
            else:
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)



print(Solution().findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
