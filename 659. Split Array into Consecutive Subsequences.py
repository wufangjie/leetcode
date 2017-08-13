class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1 = c2 = c3 = 0 # length 1, 2, other
        n = len(nums)
        i, j = 0, 1
        nums.append(nums[-1] - 1)

        while i < n:
            while nums[j] == nums[i]:
                j += 1

            c = j - i
            if nums[i] - nums[i - 1] > 1:
                if c1 > 0 or c2 > 0:
                    return False
                c1, c2, c3 = c, 0, 0
            else:
                if c1 + c2 > c:
                    return False
                left = max(0, c - c1 - c2 - c3)
                c1, c2, c3 = left, c1, c - left - c1
            i = j
            j += 1

        return c1 == c2 == 0


        # # NOTE: following method is slow when nums = [1, 2, 3, 9999997, 9999998, 9999999]
        # from collections import Counter

        # lo, hi = nums[0], nums[-1] + 1
        # count = Counter(nums)
        # c1, c2, c3 = count[lo], 0, 0 # length 1, 2, other

        # for i in range(lo + 1, hi):
        #     c = count.get(i, 0)
        #     if c1 + c2 > c:
        #         return False

        #     left = max(0, c - c1 - c2 - c3)
        #     c1, c2, c3 = left, c1, c - left - c1

        # return c1 == c2 == 0


        # lo, hi = nums[0], nums[-1] + 1
        # count = Counter(nums)

        # exist = (count[lo], 0, 0) # length 1, 2, other

        # for i in range(lo + 1, hi):
        #     c = count.get(i, 0)
        #     if exist[0] + exist[1] > c:
        #         return False

        #     left = max(0, c - sum(exist))
        #     exist = (left, exist[0], c - left - exist[0])

        # return exist[0] + exist[1] == 0



print(Solution().isPossible([1,2,3,3,4,5]), True)
print(Solution().isPossible([1,2,3,3,4,4,5,5]), True)
print(Solution().isPossible([1,2,3,4,4,5]), False)
print(Solution().isPossible([1,2]), False)
print(Solution().isPossible([1, 2, 3, 9999997, 9999998, 9999999]), True)
print(Solution().isPossible([3,4,4,5,6,7,8,9,10,11]), False)
