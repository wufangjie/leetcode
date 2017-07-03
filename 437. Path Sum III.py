from utils import TreeNode


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # map
        def dfs(node, pre_sum, count):
            if node is not None:
                cur_sum = {k + node.val: v for k, v in pre_sum.items()}
                if node.val in cur_sum:
                    cur_sum[node.val] += 1
                else:
                    cur_sum[node.val] = 1
                count[0] += cur_sum.get(sum, 0)
                dfs(node.left, cur_sum, count)
                dfs(node.right, cur_sum, count)

        count = [0]
        dfs(root, {}, count)
        return count[0]

        # lst, can know the sequence
        # def dfs(node, lst, count):
        #     if node is not None:
        #         lst.append(node.val)
        #         cumsum = 0
        #         for i in range(len(lst) - 1, -1, -1):
        #             cumsum += lst[i]
        #             if cumsum == sum:
        #                 count[0] += 1
        #         lst_for_right = lst[:]
        #         dfs(node.left, lst, count)
        #         dfs(node.right, lst_for_right, count)

        # count = [0]
        # dfs(root, [], count)
        # return count[0]


root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)),
                             TreeNode(2, None, TreeNode(1))),
                TreeNode(-3, None, TreeNode(11)))
print(Solution().pathSum(root, 8))
