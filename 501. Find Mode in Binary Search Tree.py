# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils import TreeNode


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #lct means last, count, theMax
        def inorder(node, lct, result):
            if node.left is not None:
                inorder(node.left, lct, result)

            last, count, theMax = lct
            if lct[0] == node.val:
                lct[1] += 1
            else:
                lct[:2] = node.val, 1

            if lct[1] > lct[2]:
                lct[2] = lct[1]
                # result.clear() # python2 no clear
                # result.append(node.val)
                result[:] = [node.val]
            elif lct[1] == lct[2]:
                result.append(node.val)

            if node.right is not None:
                inorder(node.right, lct, result)

        if not root:
            return []
        result = []
        inorder(root, [object(), 0, 0], result)
        return result






        # total wrong, I think the same value must be parent and child
        # def dfs(node):
        #     if node is None:
        #         return None, 0, 0, []
        #     else:
        #         lv, lo, lm, lr = dfs(node.left) # value, occur, max, result
        #         rv, ro, rm, rr = dfs(node.right)

        #         import pdb
        #         pdb.set_trace()
        #         co = 1
        #         if node.val == lv:
        #             co += lo
        #         if node.val == rv:
        #             co += ro

        #         max_child = max(lm, rm)
        #         result = [node.val]
        #         if co > max_child:
        #             return node.val, co, co, result
        #         elif co == max_child:
        #             if co == lm:
        #                 result.extend(lr)
        #             if co == rm:
        #                 result.extend(rr)
        #             return node.val, co, co, result
        #         if lm == rm:
        #             return node.val, co, lm, lr + rr
        #         elif lm > rm:
        #             return node.val, co, lm, lr
        #         else:
        #             return node.val, co, rm, rr
        # return dfs(root)[-1]


root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(2), TreeNode(6))),
                TreeNode(8, TreeNode(7), TreeNode(9)))

print(Solution().findMode(root))
