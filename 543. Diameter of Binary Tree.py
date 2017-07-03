class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        theMax = [1]
        def dfs(node):
            if node is None:
                return 0
            hl, hr = dfs(node.left), dfs(node.right)
            theMax[0] = max(theMax[0], hl + hr + 1)
            return max(hl, hr) + 1

        dfs(root)
        return theMax[0] - 1

# NOTE: return the count of path not nodes
