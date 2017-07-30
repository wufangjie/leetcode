from utils import TreeNode
from collections import defaultdict


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        count, result = defaultdict(int), []

        def dfs(node):
            if node:
                ret = '{},{},{}'.format(
                    node.val, dfs(node.left), dfs(node.right))
                count[ret] += 1
                if count[ret] == 2:
                    result.append(node)
                return ret
            else:
                return '#'

        dfs(root.left)
        dfs(root.right)
        return result



#[0,0,0,0,null,null,0,null,null,null,0]
root = TreeNode(0, TreeNode(0, TreeNode(0)),
                TreeNode(0, None, TreeNode(0, None, TreeNode(0))))
print(Solution().findDuplicateSubtrees(root))
