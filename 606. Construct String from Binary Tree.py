class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node is None:
                return ''
            right = dfs(node.right)
            left = dfs(node.left)
            if right:
                return '{}({})({})'.format(node.val, left, right)
            elif left:
                return '{}({})'.format(node.val, left)
            else:
                return str(node.val)
        return dfs(t)

            # ret = str(node.val)
            # if left or right:
            #     ret += '({})'.format(left)
            #     if right:
            #         ret += '({})'.format(right)
            # return ret



assert Solution().tree2str(None) == ''
