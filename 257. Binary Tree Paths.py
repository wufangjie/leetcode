# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, result, results):
            if result:
                result = '{}->{}'.format(result, node.val)
            else:
                result = str(node.val)
            if node.left is None and node.right is None:
                results.append(result)
            else:
                if node.left:
                    dfs(node.left, result, results)
                if node.right:
                    dfs(node.right, result, results)

        results = []
        if root:
            dfs(root, '', results)
        return results
