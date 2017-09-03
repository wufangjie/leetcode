class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        theMin = root.val
        inf = float('inf')

        def dfs(node):
            if node is None:
                return inf
            elif node.val > theMin:
                return node.val
            else:
                return min(dfs(node.left), dfs(node.right))

        ret = dfs(root)
        return -1 if ret == inf else ret



from utils import TreeNode

root = TreeNode(2, TreeNode(2, TreeNode(2), TreeNode(2)), TreeNode(2, TreeNode(2), TreeNode(2)))

print(Solution().findSecondMinimumValue(root))
