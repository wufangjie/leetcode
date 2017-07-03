class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0, 0

            ls, lt = dfs(node.left)
            rs, rt = dfs(node.right)
            return ls + rs + node.val, lt + rt + abs(ls - rs)

        return dfs(root)[1]
