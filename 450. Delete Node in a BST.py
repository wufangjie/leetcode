# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val == key:
            pre = TreeNode(float('-inf'))
            pre.right = root
            lr = 'right'
        else:
            pre = root
            while pre:
                if pre.val > key:
                    if (not pre.left) or pre.left.val != key:
                        pre = pre.left
                    else:
                        lr = 'left'
                        break
                else:
                    if (not pre.right) or pre.right.val != key:
                        pre = pre.right
                    else:
                        lr = 'right'
                        break
            else:
                return root

        cur = pre.__dict__[lr]
        if cur.left is None:
            pre.__dict__[lr] = cur.right
        elif cur.right is None:
            pre.__dict__[lr] = cur.left
        elif cur.right.left is None:
            pre.__dict__[lr] = cur.right
            cur.right.left = cur.left
        else:
            p = cur.right
            while p.left.left is not None:
                p = p.left

            pre.__dict__[lr] = rep = p.left
            p.left = rep.right
            rep.left, rep.right = cur.left, cur.right

        return pre.right if root.val == key else root


root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
head = Solution().deleteNode(root, 3)
