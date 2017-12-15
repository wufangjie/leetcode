from collections import Counter


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        seq = sorted([(key, val * key) for key, val in Counter(nums).items()])
        n = len(seq)

        def dfs(i):
            if i >= n:
                return 0
            elif i == n - 1:
                return seq[-1][1]

            if i in cache:
                return cache[i]
            if seq[i][0] == seq[i + 1][0] - 1:
                ret = max(seq[i][1] + dfs(i + 2), dfs(i + 1))
            else:
                ret = seq[i][1] + dfs(i + 1)
            cache[i] = ret
            return ret
        return dfs(0)



print(Solution().deleteAndEarn([3, 4, 2]), 6)
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)
