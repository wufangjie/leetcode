class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i, elem in enumerate(nums):
            if elem not in dct:
                dct[elem] = [i, i, 1]
            else:
                dct[elem][1] = i
                dct[elem][2] += 1
        ret = theMax = -1
        for s, e, c in dct.values():
            if c > theMax:
                ret = e - s
                theMax = c
            elif c == theMax and e - s < ret:
                ret = e - s
        return ret + 1


print(Solution().findShortestSubArray([]))
print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))
