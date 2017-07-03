'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetric_rec(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                if p.val == q.val:
                    return (isSymmetric_rec(p.left, q.right) and
                            isSymmetric_rec(p.right, q.left))
                else:
                    return False

        return isSymmetric_rec(root.left, root.right) if root else True
