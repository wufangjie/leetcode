class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        def dfs(node, d):
            if node:
                if d == 2:
                    left = TreeNode(v)
                    left.left = node.left
                    node.left = left
                    right = TreeNode(v)
                    right.right = node.right
                    node.right = right
                else:
                    dfs(node.left, d - 1)
                    dfs(node.right, d - 1)
            return node

        return dfs(root, d)
