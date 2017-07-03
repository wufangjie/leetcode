class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        neg, pos = [0] * n, [0] * n
        if nums[0] > 0:
            pos[0] = nums[0]
        else:
            neg[0] = nums[0]

        for i, elem in enumerate(nums[1:], 1):
            if elem > 0:
                pos[i] = elem * (pos[i - 1] if pos[i - 1] else 1)
                neg[i] = elem * neg[i - 1]
            elif elem < 0:
                pos[i] = elem * neg[i - 1]
                neg[i] = elem * (pos[i - 1] if pos[i - 1] else 1)
        return max(pos)


assert Solution().maxProduct([2, 3, -2, 4]) == 6
assert Solution().maxProduct([]) == 0
assert Solution().maxProduct([-2]) == -2
assert Solution().maxProduct([0, 2]) == 2
