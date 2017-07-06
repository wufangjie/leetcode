class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid = (n - 1) >> 1
        temp = sorted(nums)
        nums[::2] = temp[mid::-1]
        nums[1::2] = temp[:mid:-1]


# NOTE: not implement the follow up, but much faster
# Can you do it in O(n) time and/or in-place with O(1) extra space?

nums = [4,5,5,6]
Solution().wiggleSort(nums)
assert nums == [5, 6, 4, 5]
