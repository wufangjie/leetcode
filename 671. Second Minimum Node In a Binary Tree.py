class Solution(object):
    inf = float('inf')

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # loop version
        theMin, theMin2 = root.val, self.inf
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val <= theMin:
                if node.left:
                    stack.append(node.left)
                    stack.append(node.right)
            elif node.val < theMin2:
                theMin2 = node.val
        return -1 if theMin2 is self.inf else theMin2


        # theMin = root.val
        # inf = float('inf')

        # def dfs(node):
        #     if node is None:
        #         return inf
        #     elif node.val > theMin:
        #         return node.val
        #     else:
        #         return min(dfs(node.left), dfs(node.right))

        # ret = dfs(root)
        # return -1 if ret == inf else ret



from utils import TreeNode

root = TreeNode(2, TreeNode(2, TreeNode(2), TreeNode(2)), TreeNode(2, TreeNode(2), TreeNode(2)))

print(Solution().findSecondMinimumValue(root))
