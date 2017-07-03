'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def _get(ll, idx):
            if idx < 0:
                return -float('inf')
            try:
                return ll[idx]
            except IndexError:
                return float('inf')

        l1, l2 = len(nums1), len(nums2)
        cur_max = (l1 + l2 - 1) >> 1
        i1 = i2 = cur = 0
        while cur <= cur_max:
            if _get(nums1, i1) < _get(nums2, i2):
                i1 += 1
            else:
                i2 += 1
            cur += 1

        val = max(_get(nums1, i1 - 1), _get(nums2, i2 - 1))
        if (l1 + l2) & 1:
            return val
        else:
            return (val + min(_get(nums1, i1), _get(nums2, i2))) / 2.


if __name__ == '__main__':
    nums1, nums2 = [1, 2], [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5

    nums1, nums2 = [0, 1, 2], [0, 3, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2

    nums1, nums2 = [0, 1, 2], [0, 1.9, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 1.9

    nums1, nums2 = [0, 1, 2], [1.9, 2.1, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2

    nums1, nums2 = [0, 1, 2], [0, 0.9, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 1

    nums1, nums2 = [0, 1], [3, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) ==3

    nums1, nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [16, 17, 18, 19, 20]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 7

    nums1, nums2 = [3, 4], []
    assert Solution().findMedianSortedArrays(nums1, nums2) == 3.5

    nums1, nums2 = [], [1]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 1
