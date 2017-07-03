class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return lo + 1, hi + 1
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            else:
                hi -= 1
