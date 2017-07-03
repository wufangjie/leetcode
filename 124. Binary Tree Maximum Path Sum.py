'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
'''
from utils import TreeNode

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _nonlocal = {'max': float('-inf')}

        def _max_sum_below(node):
            # nonlocal theMax # python2 no nonlocal
            if node is None:
                return 0

            ml = _max_sum_below(node.left)
            mr = _max_sum_below(node.right)
            if ml < mr:
                ml, mr = mr, ml
            node._max = node.val + max(0, ml)
            _nonlocal['max'] = max(_nonlocal['max'], node._max + max(mr, 0))
            return node._max

        _max_sum_below(root)
        return _nonlocal['max']


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.maxPathSum(root) == 6


    root = TreeNode(-21,
                    TreeNode(-5, TreeNode(6), TreeNode(11)),
                    TreeNode(8, TreeNode(2)))
