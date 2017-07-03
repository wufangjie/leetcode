import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.idx = list(range(len(nums)))

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return [self.nums[i]
                for i in sorted(self.idx, key=lambda x: random.random())]


# random.shuffle is better
