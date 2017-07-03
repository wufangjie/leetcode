from utils import memo
import heapq


class Solution(object):
    def maxNumber(self, nums1, nums2, k):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if k == 0:
        #     return []

        # n1, n2 = len(nums1), len(nums2)

        # def rec(l1, l2, k, result, results):
        #     # print(result)
        #     if k == 0:
        #         results.append(result)
        #         return

        #     H1 = [(-elem, i) for i, elem in enumerate(nums1[l1:], l1)]
        #     heapq.heapify(H1)
        #     H2 = [(-elem, i) for i, elem in enumerate(nums2[l2:], l2)]
        #     heapq.heapify(H2)

        #     # import pdb
        #     # pdb.set_trace()
        #     while H1:
        #         e1, i1 = H1[0]
        #         if i1 >= l1 and n1 - i1 + n2 - l2 >= k:
        #             break
        #         heapq.heappop(H1)
        #     else:
        #         e1 = 1
        #     while H2:
        #         e2, i2 = H2[0]
        #         if i2 >= l2 and n1 - l1 + n2 - i2 >= k:
        #             break
        #         heapq.heappop(H2)
        #     else:
        #         e2 = 1

        #     if e1 == e2 == 1:
        #         return
        #     if e1 <= e2:
        #         rec(i1 + 1, l2, k - 1, result + [-e1], results)
        #     if e1 >= e2:
        #         rec(l1, i2 + 1, k - 1, result + [-e2], results)

        # results = []
        # rec(0, 0, k, [], results)
        # return max(results)


    def maxNumber(self, nums1, nums2, k):
        if k == 0:
            return []

        n1, n2 = len(nums1), len(nums2)
        inf = float('inf')
        # cache = {}

        bigger1 = [0] * n1
        for i in range(n1 - 2, -1, -1):
            if nums1[i] < nums1[i + 1]:
                bigger1[i] = 1
            elif nums1[i] > nums1[i + 1]:
                bigger1[i] = -1
            elif bigger1[i + 1] >= 0:
                bigger1[i] += 1
            else:
                bigger1[i] -= 1

        bigger2 = [0] * n2
        for i in range(n2 - 2, -1, -1):
            if nums2[i] < nums2[i + 1]:
                bigger2[i] = 1
            elif nums2[i] > nums2[i + 1]:
                bigger2[i] = -1
            elif bigger2[i + 1] > 0:
                bigger2[i] += 1
            elif bigger2[i + 1] < 0:
                bigger2[i] -= 1

        @memo
        def compare(l1, l2):
            if nums1[l1] > nums2[l2]:
                add = 1
            elif nums1[l1] < nums2[l2]:
                add = 2
            else:
                if bigger1[l1] == bigger2[l2]:
                    step = abs(bigger1[l1])
                    if step == 0:
                        add = 1
                    else:
                        add = compare(l1 + step, l2 + step)
                elif bigger1[l1] * bigger2[l2] <= 0:
                    add = 1 if bigger1[l1] > bigger2[l2] else 2
                else:
                    add = 1 if bigger1[l1] < bigger2[l2] else 2
            return add

        poss1, poss2 = nums1[:], nums2[:]
        for i in range(n1 - 2, -1, -1):
            poss1[i] = max(poss1[i], poss1[i + 1])
        for i in range(n2 - 2, -1, -1):
            poss2[i] = max(poss2[i], poss2[i + 1])

        @memo
        def cal(l1, l2, k):
            if k == 0:
                return []

            # if (l1, l2, k) in cache:
            #     return cache[l1, l2, k]

            left = n1 - l1 + n2 - l2 - k

            if left == 0:
                result = []
                while l1 < n1 and l2 < n2:
                    add = compare(l1, l2)
                    if add == 1:
                        result.append(nums1[l1])
                        l1 += 1
                    else:
                        result.append(nums2[l2])
                        l2 += 1

                if l1 < n1:
                    result.extend(nums1[l1:])
                else:
                    result.extend(nums2[l2:])
                return result

            gss1 = (-inf, l1)
            for i1 in range(l1, n1):
                if i1 - l1 <= left and nums1[i1] > gss1[0]:
                    gss1 = nums1[i1], i1
                    if nums1[i1] == poss1[l1]:
                        break

            gss2 = (-inf, l2)
            for i2 in range(l2, n2):
                if i2 - l2 <= left and nums2[i2] > gss2[0]:
                    gss2 = nums2[i2], i2
                    if nums2[i2] == poss2[l2]:
                        break

            if gss1[0] == gss2[0]:
                theMax = max(cal(gss1[1] + 1, l2, k - 1),
                             cal(l1, gss2[1] + 1, k - 1))
            elif gss1[0] > gss2[0]:
                theMax = cal(gss1[1] + 1, l2, k - 1)
            elif gss1[0] < gss2[0]:
                theMax = cal(l1, gss2[1] + 1, k - 1)

            #theMax = [max(gss1[0], gss2[0])] + theMax
            #cache[l1, l2, k] = theMax
            return [max(gss1[0], gss2[0])] + theMax#theMax
        return cal(0, 0, k)


    # # TLE 93/102
    # def maxNumber(self, nums1, nums2, k):
    #     if k == 0:
    #         return []

    #     n1, n2 = len(nums1), len(nums2)
    #     inf = float('inf')
    #     cache = {}

    #     def cal(l1, l2, k):
    #         if k == 0:
    #             return 0

    #         left = n1 - l1 + n2 - l2 - k
    #         if left < 0:
    #             return -inf

    #         if (l1, l2, k) in cache:
    #             return cache[l1, l2, k]

    #         gss1 = (-inf, l1)
    #         for i1 in range(l1, n1):
    #             if i1 - l1 <= left and nums1[i1] > gss1[0]:
    #                 gss1 = nums1[i1], i1
    #                 if nums1[i1] == 9:
    #                     break

    #         gss2 = (-inf, l2)
    #         for i2 in range(l2, n2):
    #             if i2 - l2 <= left and nums2[i2] > gss2[0]:
    #                 gss2 = nums2[i2], i2
    #                 if nums2[i2] == 9:
    #                     break

    #         theMax = -1
    #         if gss1[0] >= gss2[0]:
    #             theMax = max(theMax,
    #                          gss1[0] * 10 ** (k-1) + cal(gss1[1] + 1, l2, k-1))
    #         if gss1[0] <= gss2[0]:
    #             theMax = max(theMax,
    #                          gss2[0] * 10 ** (k-1) + cal(l1, gss2[1] + 1, k-1))

    #         cache[l1, l2, k] = theMax
    #         return theMax
    #     return list(map(int, str(cal(0, 0, k))))



    # # TLE 75/102
    # def maxNumber(self, nums1, nums2, k):
    #     if k == 0:
    #         return []

    #     n1, n2 = len(nums1), len(nums2)

    #     @memo
    #     def cal(l1, l2, k):
    #         if k == 0:
    #             return 0
    #         if n1 - l1 + n2 - l2 < k:
    #             return float('-inf')

    #         theMax = -1
    #         if l1 != n1:
    #             theMax = max(theMax, cal(l1+1, l2, k))
    #             if l2 >= n2 or nums1[l1] >= nums2[l2]:
    #                 theMax = max(theMax,
    #                              nums1[l1] * 10 ** (k-1) + cal(l1+1, l2, k-1))
    #         if l2 != n2:
    #             theMax = max(theMax, cal(l1, l2+1, k))
    #             if l1 >= n1 or nums1[l1] <= nums2[l2]:
    #                 theMax = max(theMax,
    #                              nums2[l2] * 10 ** (k-1) + cal(l1, l2+1, k-1))

    #         return theMax
    #     return list(map(int, str(cal(0, 0, k))))




assert Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3]
assert Solution().maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]
assert Solution().maxNumber([3, 9], [8, 9], 3) == [9, 8, 9]
import time
tic = time.time()
assert Solution().maxNumber([6,4,7,8,6,5,5,3,1,7,4,9,9,5,9,6,1,7,1,3,6,3,0,8,2,1,8,0,0,7,3,9,3,1,3,7,5,9,4,3,5,8,1,9,5,6,5,7,8,6,6,2,0,9,7,1,2,1,7,0,6,8,5,8,1,6,1,5,8,4], [3,0,0,1,4,3,4,0,8,5,9,1,5,9,4,4,4,8,0,5,5,8,4,9,8,3,1,3,4,8,9,4,9,9,6,6,2,8,9,0,8,0,0,0,1,4,8,9,7,6,2,1,8,7,0,6,4,1,8,1,3,2,4,5,7,7,0,4,8,4], 70) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 6, 5, 7, 8, 6, 6, 2, 0, 9, 7, 1, 2, 1, 7, 0, 8, 0, 6, 8, 5, 8, 1, 6, 1, 5, 8, 4, 0, 0, 0, 1, 4, 8, 9, 7, 6, 2, 1, 8, 7, 0, 6, 4, 1, 8, 1, 3, 2, 4, 5, 7, 7, 0, 4, 8, 4]
print(Solution().maxNumber([2,1,2,1,2,2,1,2,2,1,1,2,1,0,2,0,1,0,1,1,2,0,0,2,2,2,2,1,1,1,2,1,2,0,2,0,1,1,0,1,0,2,0,1,0,2,0,1,1,0,0,2,0,1,1,2,0,2,2,1,2,1,2,1,0,1,2,0,2,1,2,2,2,0,1,1,0,2,0,1,1,0,0,0,2,1,1,1,0,1,1,0,1,2,1,2,0,0,0,2,1,2,2,1,1,0,1,1,0,0,1,0,0,0,2,1,1,0,2,0,2,2,0,2,0,0,2,0,1,2,1,1,1,2,1,0,1,1,0,2,1,2,2,1,0,1,1,1,2,0,2,2,2,0,2,1,1,2,1,1,2,0,2,1,0,2,0,0,2,2,2,0,2,1,2,2,1,2,1,2,2,2,1,1,2,0,2,0,0,2,2,2,0,2,2,1,0,0,2,2,2,1,1,0,2,1,0,1,2,1,1,2,2,1,1,0,2,1,2,2,1,2,1,0,0,0,0,1,1,0,2,2,2,2,2,2,2,2,1,1,0,2,1,0,0,0,0,2,1,1], [1,1,0,2,0,1,1,1,0,2,2,2,1,1,0,1,2,1,2,1,0,1,2,2,2,2,1,1,0,2,0,1,0,0,1,1,0,1,2,1,2,1,2,0,1,1,1,1,2,0,1,1,1,0,0,1,0,1,2,1,1,0,2,2,1,2,0,2,0,1,1,2,0,1,1,2,2,1,0,1,2,2,0,1,1,2,2,0,2,2,0,2,1,0,0,2,1,0,0,2,1,2,1,2,0,2,0,1,1,2,1,1,1,2,0,2,2,0,2,2,0,2,1,2,1,2,0,2,0,0,1,2,2,2,2,1,2,2,0,1,0,0,2,2,2,2,0,1,0,2,1,2,2,2,1,1,1,1,2,0,0,1,0,0,2,2,1,0,0,1,1,0,0,1,1,0,2,2,2,2,2,1,0,2,2,0,0,1,0,0,1,1,1,2,2,0,0,2,0,0,0,1,2,0,2,0,1,2,0,1,2,0,1,1,0,0,1,2,1,0,2,1,0,1,2,0,1,1,2,1,0,2,1,2,1,1,0,2,2,1,0,2,1,1,1,0,0,0,1,0], 500)) == [2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 0, 2, 0, 2, 0, 1, 1, 1, 0, 2, 2, 2, 1, 1, 0, 1, 2, 1, 2, 1, 0, 1, 2, 2, 2, 2, 1, 1, 0, 2, 0, 1, 0, 1, 1, 2, 0, 1, 0, 0, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 0, 2, 0, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 1, 0, 0, 2, 0, 1, 1, 2, 0, 2, 2, 1, 2, 1, 2, 1, 0, 1, 2, 0, 2, 1, 2, 2, 2, 0, 1, 1, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0, 0, 1, 0, 1, 2, 1, 1, 0, 2, 2, 1, 2, 0, 2, 0, 1, 1, 2, 0, 1, 1, 2, 2, 1, 0, 1, 2, 2, 0, 1, 1, 2, 2, 0, 2, 2, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 2, 1, 2, 0, 2, 0, 1, 1, 2, 1, 1, 1, 2, 0, 2, 2, 0, 2, 2, 0, 2, 1, 2, 1, 2, 0, 2, 0, 0, 1, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 0, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 0, 0, 1, 0, 0, 2, 2, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 2, 2, 2, 2, 2, 1, 0, 2, 2, 0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 0, 0, 2, 0, 0, 0, 2, 1, 1, 1, 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 2, 1, 1, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 1, 2, 1, 1, 1, 2, 1, 0, 1, 1, 0, 2, 1, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 2, 2, 0, 2, 1, 1, 2, 1, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2, 2, 2, 0, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 0, 2, 0, 0, 2, 2, 2, 0, 2, 2, 1, 0, 0, 2, 2, 2, 1, 1, 0, 2, 1, 0, 1, 2, 1, 1, 2, 2, 1, 1, 0, 2, 1, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 0, 0, 1, 2, 1, 0, 2, 1, 0, 1, 2, 0, 1, 1, 2, 1, 0, 2, 1, 2, 1, 1, 0, 2, 2, 1, 0, 2, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 2, 1, 0, 0, 0, 0, 2, 1, 1, 0]
print(time.time() - tic)
