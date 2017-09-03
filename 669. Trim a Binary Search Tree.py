class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)

        self.dfs_left(root, L)
        self.dfs_right(root, R)
        return root

    def dfs_left(self, node, L):
        if node:
            if node.val >= L:
                node.left = self.dfs_left(node.left, L)
                return node
            else:
                return self.dfs_left(node.right, L)

    def dfs_right(self, node, R):
        if node:
            if node.val <= R:
                node.right = self.dfs_right(node.right, R)
                return node
            else:
                return self.dfs_right(node.left, R)



from utils import TreeNode
root = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
print(Solution().trimBST(root, 1, 3))
