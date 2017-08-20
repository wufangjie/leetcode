class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        subSum = set()

        def dfs(node):
            if node is None:
                return 0
            ret = node.val + dfs(node.left) + dfs(node.right)
            if node is not root:
                subSum.add(ret)
            return ret

        total = dfs(root)
        if total & 1:
            return False
        else:
            return total >> 1 in subSum

# maybe float, but those static language's defination is int
# and the change is easy

from utils import TreeNode
root = TreeNode(5, TreeNode(10, TreeNode(10, TreeNode(2), TreeNode(3))))

print(Solution().checkEqualTree(root))
