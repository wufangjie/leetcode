from utils import TreeNode


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        left, right = [], []
        node = root
        while node:
            left.append(node)
            node = node.left
        node = root
        while node:
            right.append(node)
            node = node.right

        while left[-1].val < right[-1].val:
            if left[-1].val + right[-1].val == k:
                return True
            elif left[-1].val + right[-1].val < k:
                node = left.pop().right
                while node:
                    left.append(node)
                    node = node.left
            else:
                node = right.pop().left
                while node:
                    right.append(node)
                    node = node.right
        return False



root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                TreeNode(6, None, TreeNode(7)))

print(Solution().findTarget(root, 9))
print(Solution().findTarget(root, 28))
print(Solution().findTarget(root, 6))
