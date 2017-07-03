class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = TreeNode(0)
        dummy.right = root
        result = []
        stack = [dummy]
        while stack:
            current = stack.pop()
            result.append(current.val)
            node = current.right
            while node:
                stack.append(node)
                node = node.left
        return result[1:]
