# only in python2. python3 use __lt__, __eq__ instead
from itertools import chain, izip


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(map(str, nums), cmp=self.compare, reverse=True)
        if nums[0] == '0':
            return '0'
        return ''.join(nums)

    @staticmethod
    def compare(str1, str2):
        for c1, c2 in izip(chain(str1, str2), chain(str2, str1)):
            if c1 < c2:
                return -1
            elif c1 > c2:
                return 1
        return 0



if __name__ == '__main__':
    assert Solution().largestNumber([0, 0]) == '0'
