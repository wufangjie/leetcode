class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ii, jj = 0, len(nums) - 1
        idx = sorted(range(jj + 1), key=lambda x: nums[x])
        while ii < jj:
            if nums[idx[ii]] + nums[idx[jj]] == target:
                return idx[ii], idx[jj]
            elif nums[idx[ii]] + nums[idx[jj]] < target:
                ii += 1
            else:
                jj -= 1

if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == (0, 1)
    assert Solution().twoSum([2, 7, 7, 11, 15], 14) == (1, 2)
