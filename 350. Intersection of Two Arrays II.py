from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dct1, dct2 = defaultdict(int), defaultdict(int)
        for elem in nums1:
            dct1[elem] += 1
        for elem in nums2:
            dct2[elem] += 1

        result = []
        for k in dct1:
            if k in dct2:
                result.extend([k] * min(dct1[k], dct2[k]))
        return result


print(Solution().intersect([1, 2, 2, 1], [2, 2, 1, 0]))
