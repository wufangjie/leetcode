class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def dfs(i, count):
            if count == n:
                return 1
            if nums[i] % n == 0:
                return 0
            else:
                nxt = (i + nums[i]) % n
                if nums[nxt] * nums[i] > 0:
                    nums[i] = dfs(nxt, count + 1)
                else:
                    nums[i] = 0
                return nums[i]

        for i, elem in enumerate(nums):
            if elem != 0:
                if dfs(i, 0):
                    return True
        return False

# NOTE: The loop must be "forward" or "backward'
assert Solution().circularArrayLoop([2, -1, 1, 2, 2])
assert not Solution().circularArrayLoop([-1, 2])
assert not Solution().circularArrayLoop([-2, 1, -1, -2, -2])
