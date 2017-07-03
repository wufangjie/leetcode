from utils import TreeNode


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0, 0
            vl, bl = dfs(node.left)
            vr, br = dfs(node.right)
            return vl + vr + (node.left.val if bl == 1 else 0), bl + br + 1
        return dfs(root)[0]
