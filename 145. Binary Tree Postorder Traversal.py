from utils import TreeNode

# postorder 注意是后序, inorder 才是中序

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return result[::-1]

# I submit this code twice, get
# 119ms beat 0%
# 36ms beat 96.29%

Solution().postorderTraversal(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)))
