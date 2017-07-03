from utils import TreeNode


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, acc):
            if node is None:
                return acc
            node.val += dfs(node.right, acc)
            return dfs(node.left, node.val)
        dfs(root, 0)
        return root
