import bisect


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]

        i = bisect.bisect_left(arr, x)
        n = len(arr)
        if i == n:
            return arr[-k:]

        if x - arr[i - 1] <= arr[i] - x:
            i -=  1

        lo, hi = i - 1, i + 1
        k2 = k
        while k2 > 1:
            if lo == -1:
                return arr[:k]
            elif hi == n:
                return arr[-k:]

            if x - arr[lo] > arr[hi] - x:
                hi += 1
            else:
                lo -= 1
            k2 -= 1
        return arr[lo+1 : hi]


# import numpy as np
arr = [1, 2, 2, 3, 9, 13, 15, 16, 18, 23, 25, 30, 37, 42, 48, 52, 53, 55, 61, 74, 74, 75, 81, 82, 84, 92, 94, 96, 96, 96, 98]
#arr = np.sort(np.random.randint(0, 99, 30))
print(Solution().findClosestElements(arr, 3, 97))
print(Solution().findClosestElements(arr, 2, 3))
print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))
