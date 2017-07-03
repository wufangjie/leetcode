# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, result):
            if node is None:
                result.append('#')
            else:
                result.append(str(node.val))
                dfs(node.left, result)
                dfs(node.right, result)
        result = []
        dfs(root, result)
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        stack = [TreeNode(0)]
        data_list = data.split(',')
        i, n = 0, len(data_list)
        while i < n:
            if data_list[i] != '#':
                node = TreeNode(data_list[i])
                stack[-1].left = node
                stack.append(node)
            else:
                while i < n and data_list[i] == '#':
                    i += 1
                    node = stack.pop()
                if i == n:
                    return node.left
                node.right = TreeNode(data_list[i])
                stack.append(node.right)
            i += 1




# Your Codec object will be instantiated and called as such:
root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                TreeNode(4, TreeNode(5, TreeNode(6)),
                         TreeNode(7, None, TreeNode(8, TreeNode(9)))))
codec = Codec()
seq = codec.serialize(root)
print(seq)
head = codec.deserialize(seq)
