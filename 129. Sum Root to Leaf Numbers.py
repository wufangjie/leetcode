from utils import TreeNode

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _nonlocal = {'sum': 0}
        def dfs(node, pathSum):
            pathSum = 10 * pathSum + node.val
            if node.left is None and node.right is None:
                _nonlocal['sum'] += pathSum
            else:
                if node.left:
                    dfs(node.left, pathSum)
                if node.right:
                    dfs(node.right, pathSum)

        if root:
            dfs(root, 0)
        return _nonlocal['sum']


root = TreeNode(1, TreeNode(2), TreeNode(3))#, TreeNode(4)))
print(Solution().sumNumbers(root))
