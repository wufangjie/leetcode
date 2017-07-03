from utils import memo

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        @memo
        def rob_rec(i, used0): # from position i to end
            if i == n - 2 - used0:
                return max(nums[i], nums[i+1])
            elif i == n - 1 - used0:
                return nums[i]
            elif i > n - 1 - used0:
                return 0
            if nums[i] >= nums[i + 1]:
                return nums[i] + rob_rec(i + 2, used0)
            elif nums[i + 1] >= nums[i] + nums[i + 2]:
                return nums[i + 1] + rob_rec(i + 3, used0)
            else:
                return max(nums[i] + rob_rec(i + 2, used0),
                           nums[i + 1] + rob_rec(i + 3, used0))
        return max(nums[0] + rob_rec(2, 1), rob_rec(1, 0))


if __name__ == '__main__':
    import numpy as np
    nums = np.random.randint(0, 99, 500)
    print(Solution().rob(nums))
