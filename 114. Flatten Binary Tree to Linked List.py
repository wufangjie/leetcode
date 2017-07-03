'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(node, dd):
            if node:
                dd['pre'].right = node
                dd['pre'].left = None
                dd['pre'] = node
                right = node.right
                dfs(node.left, dd)
                dfs(right, dd)

        dummy = TreeNode(None)
        dd = {'pre': dummy}
        dfs(root, dd)
        dd['pre'].left = dd['pre'].right = None
        return dummy.right


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    Solution().flatten(root)
