from utils import TreeNode


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False

        if self.dfs(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def dfs(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        else:
            if s.val != t.val:
                return False
            else:
                return self.dfs(s.left, t.left) and self.dfs(s.right, t.right)
