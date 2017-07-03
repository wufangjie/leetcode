class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major = [None, None]
        count = [0, 0]
        for elem in nums:
            if elem == major[0]:
                count[0] += 2
                count[1] -= 1
            elif elem == major[1]:
                count[0] -= 1
                count[1] += 2
            else:
                count[0] -= 1
                count[1] -= 1

                if min(count) < 0:
                    i = count[0] > count[1]
                    major[i] = elem
                    count[i] += 3

        return [major[i] for i in range(2)
                if count[i] > 0 and nums.count(major[i]) > len(nums) // 3]



import numpy as np
from collections import Counter

#a = np.random.randint(0, 3, 20)
Solution().majorityElement(a)
