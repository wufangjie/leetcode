class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 39ms
        # nums.append(None)
        # for i in range(0, len(nums), 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]

        # 32ms
        return 2 * sum(nums[::2]) - sum(nums)

        # # 52ms
        # ret = 0
        # for elem in nums:
        #     ret ^= elem
        # return ret
