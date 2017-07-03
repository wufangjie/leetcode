'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {} # elem: [start, end]
        theMax = 0
        for elem in nums:
            if result.get(elem) is None:
                if (result.get(elem - 1) is None and
                    result.get(elem + 1) is None):
                    result[elem] = [elem, elem]
                elif result.get(elem - 1) is None:
                    i2 = result[elem + 1][1]
                    result[i2][0] = elem
                    result[elem] = result[i2]
                elif result.get(elem + 1) is None:
                    i1 = result[elem - 1][0]
                    result[i1][1] = elem
                    result[elem] = result[i1]
                else:
                    i1, i2 = result[elem - 1][0], result[elem + 1][1]
                    result[elem] = result[i1] = result[i2] = [i1, i2]
                theMax = max(theMax, result[elem][1] - result[elem][0] + 1)
        return theMax


if __name__ == '__main__':
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([]) == 0
