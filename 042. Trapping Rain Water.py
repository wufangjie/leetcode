'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0

        lo, hi = 0, n - 1
        sum_left = sum_right = sum_temp = 0
        h_left, h_right = height[0], height[-1]
        while lo <= hi:
            if h_left < h_right:
                while lo <= hi:
                    lo += 1
                    if height[lo] >= h_left:
                        h_left = height[lo]
                        sum_left += sum_temp
                        sum_temp = 0
                        break
                    else:
                        sum_temp += h_left - height[lo]
            else:
                while lo <= hi:
                    hi -= 1
                    if height[hi] >= h_right:
                        h_right = height[hi]
                        sum_right += sum_temp
                        sum_temp = 0
                        break
                    else:
                        sum_temp += h_right - height[hi]
        return sum_left + sum_right


if __name__ == '__main__':
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
