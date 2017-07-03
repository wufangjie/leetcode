import bisect


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        count = acc = 0
        pre = []
        for elem in nums:
            i = bisect.bisect_left(pre, lower - acc - elem)
            j = bisect.bisect_right(pre, upper - acc - elem)
            count += j - i
            if lower <= elem <= upper:
                count += 1

            bisect.insort(pre, -acc)
            acc += elem
        return count


print(Solution().countRangeSum([-2, 5, -1], -2, 2))
