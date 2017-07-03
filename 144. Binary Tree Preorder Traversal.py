# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None):
        self.val = x
        self.left = left
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result




        # only python3
        # def dfs(node):
        #     if node:
        #         yield node.val
        #         yield from dfs(node.left)
        #         yield from dfs(node.right)
        # return list(dfs(root))


Solution().preorderTraversal(TreeNode(1, TreeNode(2)))
