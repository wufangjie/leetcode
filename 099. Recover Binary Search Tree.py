'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(node, dd):
            if node:
                dfs(node.left, dd)

                if dd['finished']:
                    return
                elif dd['big']:
                    if node.val < dd['pre'].val:
                        node.val, dd['big'].val = dd['big'].val, node.val
                        dd['finished'] = True
                    else:
                        dd['pre'] = node
                else:
                    if node.val < dd['pre'].val:
                        dd['big'] = dd['pre']
                        dd['next'] = node
                    dd['pre'] = node

                dfs(node.right, dd)
        dd = {'pre': TreeNode(float('-inf')), 'big': None, 'finished': False}
        dfs(root, dd)
        if not dd['finished']:
            dd['next'].val, dd['big'].val = dd['big'].val, dd['next'].val
        # import pdb
        # pdb.set_trace()
        # print('hello world!')



def inorder(root):
    def dfs(node, results):
        if node:
            dfs(node.left, results)
            results.append(node.val)
            dfs(node.right, results)

    results = []
    dfs(root, results)
    return results


if __name__ == '__main__':

    a = TreeNode(0)
    b = TreeNode(1)
    a.left = b
    Solution().recoverTree(a)
