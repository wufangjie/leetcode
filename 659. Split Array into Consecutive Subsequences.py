from collections import Counter


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lo, hi = nums[0], nums[-1] + 1
        count = Counter(nums)

        exist = (count[lo], 0, 0) # length 1, 2, other

        for i in range(lo + 1, hi):
            c = count.get(i, 0)
            if exist[0] + exist[1] > c:
                return False

            left = max(0, c - sum(exist))
            exist = (left, exist[0], c - left - exist[0])

        return exist[0] + exist[1] == 0



print(Solution().isPossible([1,2,3,3,4,5]), True)
print(Solution().isPossible([1,2,3,3,4,4,5,5]), True)
print(Solution().isPossible([1,2,3,4,4,5]), False)

print(Solution().isPossible([1,2]))
