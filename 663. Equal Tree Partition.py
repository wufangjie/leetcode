# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        subSum = []

        def dfs(node):
            if node is None:
                return 0
            else:
                subSum.append(node.val + dfs(node.left) + dfs(node.right))
                return subSum[-1]

        dfs(root)
        if subSum[-1] & 1:
            return False
        elif subSum[-1] == 0:
            return 0 in subSum[:-1]
        else:
            return subSum[-1] // 2 in subSum



root = TreeNode(5, TreeNode(10, TreeNode(10, TreeNode(2), TreeNode(3))))

print(Solution().checkEqualTree(root))
