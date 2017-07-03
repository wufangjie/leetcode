'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        theBest = float('-inf')
        tempSum = 0
        for elem in nums:
            if theBest < 0:
                theBest = max(theBest, elem)
            elif elem < 0:
                theBest = max(theBest, tempSum)
            if tempSum + elem <= 0:
                tempSum = 0
            else:
                tempSum += elem
        return theBest if theBest < 0 else max(theBest, tempSum)


if __name__ == '__main__':
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-2, -1]) == -1
