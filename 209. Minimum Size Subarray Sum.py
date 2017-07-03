class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        theSum = 0
        length = len(nums)
        minLen = 2 * length
        for i, elem in enumerate(nums):
            theSum += elem
            if i - minLen >= 0:
                theSum -= nums[i - minLen]
            if theSum >= s:
                for j in range(max(0, i - minLen + 1), i):
                    theSum -= nums[j]
                    if theSum < s:
                        break
                else:
                    return 1
                minLen = i - j
        return 0 if minLen >= length else minLen + 1


if __name__ == '__main__':
    assert Solution().minSubArrayLen(20, [7, 3, 2, 3, 9, 5, 5, 5, 8, 8, 4, 8, 3, 1, 3, 8, 4, 3, 3, 2]) == 3
    assert Solution().minSubArrayLen(93, [7, 3, 2, 3, 9, 5, 5, 5, 8, 8, 4, 8, 3, 1, 3, 8, 4, 3, 3, 2]) == 20
    assert Solution().minSubArrayLen(95, [7, 3, 2, 3, 9, 5, 5, 5, 8, 8, 4, 8, 3, 1, 3, 8, 4, 3, 3, 2]) == 0
    assert Solution().minSubArrayLen(100, []) == 0
