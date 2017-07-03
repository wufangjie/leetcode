# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]


    def hasNext(self):
        """
        :rtype: bool
        """
        l = len(self.stack)
        return l > 1 or (l == 1 and self.stack[-1].right)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return self.stack[-1].val



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# [4,3,7,null, 3.5, 5, 15, null, null, 4.5]
root = TreeNode(4, TreeNode(3, None, TreeNode(3.5)), TreeNode(7, TreeNode(5, TreeNode(4.5)), TreeNode(15)))
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
