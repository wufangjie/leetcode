# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode, memo


def get_val(node, mode='self'):
    if node is None:
        return 0
    elif mode == 'self':
        return node.val
    else:
        return get_val(node.left) + get_val(node.right)


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        @memo
        def rec(node, can_rob=False):
            if not node:
                return 0
            elif can_rob:
                left, right = node.left, node.right
                return max((left.val if left else 0) + rec(right, True)
                           + (rec(left.left) + rec(left.right) if left else 0),
                           (right.val if right else 0) + rec(left, True)
                           + (rec(right.left) + rec(right.right) if right else 0),
                           node.val + rec(left) + rec(right))

                # I think more prune will be a bit more faster, but may not
                # left, right = get_val(node.left), get_val(node.right)
                # if node.val >= left + right:
                #     return node.val + rec(node.left) + rec(node.right)
                # else:
                #     ret = max(left + rec(node.right, True)
                #               + (rec(node.left.left) + rec(node.left.right)
                #                  if node.left else 0),
                #               right + rec(node.left, True)
                #               + (rec(node.right.left) + rec(node.right.right)
                #                  if node.right else 0))

                #     if (left < node.val + get_val(node.left, 'child')
                #         and right < node.val + get_val(node.right, 'child')):
                #         ret = max(ret,
                #                   node.val + rec(node.left) + rec(node.right))
                #     return ret
            else:
                return rec(node.left, True) + rec(node.right, True)
        return rec(root, True)



root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
print(Solution().rob(root))
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
print(Solution().rob(root))

root = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3))
print(Solution().rob(root))
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
print(Solution().rob(root))
