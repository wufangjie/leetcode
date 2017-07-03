class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = len(nums)
        theMax = 0
        for i, elem in enumerate(nums):
            if elem > -1:
                count = 1
                while elem != i:
                    temp = nums[elem]
                    nums[elem] = -1
                    elem = temp
                    count += 1

                left -= count
                theMax = max(theMax, count)
                if left <= theMax:
                    return theMax


print(Solution().arrayNesting([1,0,2,3,4]))
print(Solution().arrayNesting([5,4,0,3,1,6,2]))
