from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        Q = deque([root, None])
        acc = count = 0
        while True:
            node = Q.popleft()
            if node is None:
                result.append((acc + 0.) / count)
                if Q:
                    Q.append(None)
                    acc = count = 0
                else:
                    return result
            else:
                acc += node.val
                count += 1
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
