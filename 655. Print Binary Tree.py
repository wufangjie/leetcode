from utils import TreeNode


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def dfs_height(node):
            if node is None:
                return 0
            return max(dfs_height(node.left), dfs_height(node.right)) + 1

        h = dfs_height(root)
        n = 2 ** h - 1
        ret = [[''] * n for _ in range(h)]

        def dfs_print(node, lo, hi, level):
            if node:
                mid = (lo + hi) >> 1
                ret[level][mid] = str(node.val)
                dfs_print(node.left, lo, mid - 1, level + 1)
                dfs_print(node.right, mid + 1, hi, level + 1)

        dfs_print(root, 0, n, 0)
        return ret


root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))),
                TreeNode(5))
from pprint import pprint
pprint(Solution().printTree(root))
