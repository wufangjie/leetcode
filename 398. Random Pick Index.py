import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 1
        ret = -1
        for i, elem in enumerate(self.nums):
            if elem == target:
                if random.random() < 1. / count:
                    ret = i
                count += 1
        return ret


# NOTE: The array size can be very large. Solution that uses too much extra space will not pass the judge.


# # Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])
print(Counter(obj.pick(3) for _ in range(5000)))

# # param_1 = obj.pick(target)

from collections import Counter
