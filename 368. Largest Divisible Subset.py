class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        count, pre = [1] * n, [-1] * n
        theMax = (0, -1)
        for i in range(n):
            for j in range(i):
                if count[j] + 1 >= count[i] and nums[i] % nums[j] == 0:
                    count[i] = count[j] + 1
                    pre[i] = j
            theMax = max(theMax, (count[i], i))

        l, i = theMax
        result = [0] * l
        while l > 0:
            l -= 1
            result[l] = nums[i]
            i = pre[i]
        return result



print(Solution().largestDivisibleSubset([1, 2, 3]))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
