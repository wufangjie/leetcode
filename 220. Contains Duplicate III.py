def exist_in_k(a, x, lo, hi, k):
    while lo < hi:
        mid = (lo + hi) >> 1
        if abs(a[mid] - x) <= k:
            return True
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t == 0:
            last_met = {}
            for i, elem in enumerate(nums):
                if elem in last_met and i - last_met[elem] <= k:
                    return True
                last_met[elem] = i
            return False

        index = sorted(range(len(nums)), key=lambda x: (nums[x], x))
        data = [[float('-inf')] * 2] # value, index
        for idx in index:
            elem = nums[idx]
            for j in range(len(data) - 1, 0, -1):
                if elem - data[j][0] <= t:
                    if exist_in_k(data[j], idx, 1, len(data[j]), k):
                        return True
                else:
                    break
            if data[-1][0] == elem:
                data[-1].append(idx)
            else:
                data.append([elem, idx])
        return False

        # TLE
        # import bisect
        # data = []
        # for i, elem in enumerate(nums):
        #     n = len(data)
        #     j = idx = bisect.bisect_right(data, [elem, i])
        #     for j in range(idx, n):
        #         if data[j][0] - elem <= t:
        #             if i - data[j][1] <= k:
        #                 return True
        #         else:
        #             break
        #     for j in range(idx-1, -1, -1):
        #         if elem - data[j][0] <= t:
        #             if i - data[j][1] <= k:
        #                 return True
        #         else:
        #             break
        #     if idx < n and data[idx][0] == elem:
        #         data[idx][1] = i
        #     else:
        #         data.insert(idx, [elem, i])
        # return False


# import numpy as np
# a = np.random.randint(0, 99, 20)
# print(a)
# Solution().containsNearbyAlmostDuplicate(a, 3, 3)
