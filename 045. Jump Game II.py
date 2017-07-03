'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        far = nums[0] + 1
        i = count = 1
        while True:
            if far >= n:
                return count

            count += 1
            for j in range(i, far):
                far = max(far, j + nums[j] + 1)
            i = j + 1
            if i >= far:
                raise Exception('cannot reach')


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump(list(range(25000, 0, -1)) + [1, 0]) == 1
    assert Solution().jump([1] * 25000)
