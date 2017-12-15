# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode


class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        parent = []
        def dfs(node):
            if node.left is None and node.right is None:
                h, v, has_k_offspring = -1, node.val, node.val == k
            elif node.left is None:
                h, v, has_k_offspring = dfs(node.right)
            elif node.right is None:
                h, v, has_k_offspring = dfs(node.left)
            else:
                hl, vl, has_k_l = dfs(node.right)
                hr, vr, has_k_r = dfs(node.left)
                h = min(hl, hr)
                v = vl if hl < hr else vr
                has_k_offspring = has_k_l + has_k_r

            h += 1
            has_k_offspring |= (node.val == k)

            if has_k_offspring:
                parent.append((h + len(parent), v))
            return h, v, has_k_offspring

        dfs(root)
        return min(parent)[1]



# root = TreeNode(1, TreeNode(3), TreeNode(2))
# print(Solution().findClosestLeaf(root, 1))


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6, TreeNode(8), TreeNode(9))), TreeNode(5, None, TreeNode(7, TreeNode(10)))))
print(Solution().findClosestLeaf(root, 3))
