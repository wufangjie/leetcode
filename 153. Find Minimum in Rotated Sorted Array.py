# You may assume no duplicate

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        if nums[hi] >= nums[lo]:
            return nums[lo]
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] > nums[lo]:
                lo = mid
            else:
                hi = mid
        return nums[lo+1]


if __name__ == '__main__':
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([0, 1, 2]) == 0
    assert Solution().findMin([0]) == 0
    assert Solution().findMin([]) == 0
