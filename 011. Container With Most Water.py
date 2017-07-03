'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        theBest = 0
        while lo < hi:
            theBest = max(theBest, (hi - lo) * min(height[lo], height[hi]))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return theBest


    def maxArea_TLE2(self, height):
        maxlen = len(height)

        def _max_area_as_short_side(i):
            left = right = 0
            for j in range(i):
                if height[j] >= height[i]:
                    left = height[i] * (i - j)
                    break
            for j in range(maxlen - 1, i, -1):
                if height[j] >= height[i]:
                    right = height[i] * (j - i)
                    break
            return max(left, right)

        theBest = maxHeight = 0
        for i in range(maxlen >> 1):
            if height[i] < maxHeight:
                continue
            else:
                maxHeight = height[i]
                theBest = max(theBest, _max_area_as_short_side(i))
        left = theBest
        theBest = maxHeight = 0
        for i in range(maxlen - 1, (maxlen >> 1) - 1, -1):  # the mid ()
            if height[i] < maxHeight:
                continue
            else:
                maxHeight = height[i]
                theBest = max(theBest, _max_area_as_short_side(i))
        return max(left, theBest)


    def maxArea_TLE(self, height):
        maxlen = len(height)

        def _max_area_as_short_side(i):
            left = right = 0
            for j in range(i):
                if height[j] >= height[i]:
                    left = height[i] * (i - j)
                    break
            for j in range(maxlen - 1, i, -1):
                if height[j] >= height[i]:
                    right = height[i] * (j - i)
                    break
            return max(left, right)
        return max([_max_area_as_short_side(i) for i in range(maxlen)])

if __name__ == '__main__':
    assert Solution().maxArea([2, 1]) == 1
    assert Solution().maxArea(range(15001))
