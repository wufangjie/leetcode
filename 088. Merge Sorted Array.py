'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''


# NOTE: len(nums1) >= m + n and nums1[:m] is the sorted array you should merge

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        nums1[n:n + m] = nums1[:m]
        cur1, cur2, cur = n, 0, 0
        while cur1 < m + n and cur2 < n:
            if nums1[cur1] > nums2[cur2]:
                nums1[cur] = nums2[cur2]
                cur2 += 1
            else:
                nums1[cur] = nums1[cur1]
                cur1 += 1
            cur += 1
        if cur2 < n:
            nums1[cur:m + n] = nums2[cur2:n]


if __name__ == '__main__':
    nums1 = [2, 0, 0, 0, 0]
    Solution().merge(nums1, 1, [3, 4, 5], 2)
    print(nums1)
