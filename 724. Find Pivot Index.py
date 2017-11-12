class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        pre = 0
        for i, elem in enumerate(nums):
            if (pre << 1) == total - elem:
                return i
            pre += elem
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, -1, 3]))
print(Solution().pivotIndex([1]))
print(Solution().pivotIndex([]))
