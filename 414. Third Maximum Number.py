class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = float('-inf')
        for elem in nums:
            if elem > max1:
                max1, max2, max3 = elem, max1, max2
            elif max1 > elem > max2:
                max2, max3 = elem, max2
            elif max2 > elem > max3:
                max3 = elem
        return max1 if max3 == float('-inf') else max3


        # theMax = [float('-inf')] * 3
        # for elem in nums:
        #     if elem not in theMax:
        #         if elem > theMax[0]:
        #             theMax[1:] = theMax[:2]
        #             theMax[0] = elem
        #         elif elem > theMax[1]:
        #             theMax[1], theMax[2] = elem, theMax[1]
        #         elif elem > theMax[2]:
        #             theMax[2] = elem
        # return theMax[0] if theMax[2] == float('-inf') else theMax[2]
