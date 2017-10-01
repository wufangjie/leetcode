# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from utils import TreeNode

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        theMax = [0]
        def dfs(node):
            if node:
                lv, ll = dfs(node.left)
                rv, rl = dfs(node.right)
                v, l, l2 = node.val, 0, 0
                if lv != v:
                    if rv == v:
                        l += rl + 1
                else:
                    if rv != v:
                        l += ll + 1
                    else:
                        l += max(ll, rl) + 1
                        l2 = ll + rl + 2
                theMax[0] = max(l, l2, theMax[0])
                return v, l
            return None, 0
        dfs(root)
        return theMax[0]


root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)),
                TreeNode(5, None, TreeNode(5)))
print(Solution().longestUnivaluePath(root))
