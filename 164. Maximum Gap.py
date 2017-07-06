class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        theMin, theMax = min(nums), max(nums)
        step = (theMax - theMin) // n + 1
        result = [None] * n
        for elem in nums:
            i = (elem - theMin) // step
            if not result[i]:
                result[i] = [elem, elem]
            elif elem < result[i][0]:
                result[i][0] = elem
            elif elem > result[i][1]:
                result[i][1] = elem
        pre = theMin
        ret = 0
        for comb in result:
            if comb:
                ret = max(ret, comb[0] - pre)
                pre = comb[1]
        return ret

        # theMin, theMax = min(nums), max(nums)
        # step = (theMax - theMin) // n + 1
        # result = [[] for _ in range(n)]
        # for elem in nums:
        #     i = (elem - theMin) // step
        #     result[i].append(elem)
        # pre = theMin
        # ret = 0
        # for comb in result:
        #     if comb:
        #         tempMin, tempMax = min(comb), max(comb)
        #         ret = max(ret, tempMin - pre)
        #         pre = tempMax
        # return ret



#print(Solution().maximumGap([]))
print(Solution().maximumGap([33, 94, 80, 72, 41, 48, 56, 1, 37, 15, 69, 57, 79, 51, 21, 34, 19, 41, 44, 6]))
