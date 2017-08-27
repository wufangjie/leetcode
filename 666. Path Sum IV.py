class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for elem in nums:
            d, p, v = map(int, str(elem))
            dct[d, p] = v

        def dfs(d, p):
            if (d, p) not in dct:
                return 0, 0

            v = dct[d, p]
            d += 1
            p <<= 1
            left_sum, left_leaves = dfs(d, p - 1)
            right_sum, right_leaves = dfs(d, p)
            leaves = max(1, left_leaves + right_leaves)
            return left_sum + right_sum + v * leaves, leaves
        return dfs(1, 1)[0]

print(Solution().pathSum([113, 215, 221]))
print(Solution().pathSum([113, 221]))
