from collections import defaultdict, Counter
from copy import deepcopy
from utils import memo


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # # TLE 20/60
        # @memo
        # def dfs(*boxes):
        #     if not boxes:
        #         return 0

        #     dct = defaultdict(list)
        #     pre = 0
        #     for i, b in enumerate(boxes):
        #         if i == 0 or b != boxes[i - 1]:
        #             dct[b].append([i, i+1])
        #             pre = i
        #         else:
        #             dct[b][-1][1] += 1

        #     idx, to_remove = set(), set()
        #     ret = 0
        #     for k, v in dct.items():
        #         if len(v) == 1:
        #             to_remove.add(k)
        #             lo, hi = v[0]
        #             idx.update(range(lo, hi))
        #             ret += (hi - lo) ** 2

        #     if ret:
        #         return ret + dfs(
        #             *(boxes[i] for i in range(len(boxes)) if i not in idx))

        #     for k, vs in dct.items():
        #         for lo, hi in vs:
        #             ret = max(
        #                 ret, (hi - lo) ** 2 + dfs(*(boxes[:lo] + boxes[hi:])))
        #     return ret

        # return dfs(*boxes)


        # # TLE 20/60
        # n = len(boxes)
        # first_value, last_first = {}, {}
        # dct = defaultdict(dict) # {val: {lo: [hi, step]}}
        # pre = 0
        # for i, b in enumerate(boxes):
        #     if i == 0 or b != boxes[i - 1]:
        #         first_value[i] = b
        #         dct[b][i] = [i+1, 1]
        #         last_first[i] = pre
        #         pre = i
        #     else:
        #         dct[b][pre][0] += 1
        #         dct[b][pre][1] += 1

        # def remove(k, lo, dct, first_value, last_first):
        #     hi, count = dct[k][lo]
        #     lolo = last_first[lo]
        #     if hi != n:
        #         val = first_value[hi]
        #         change = dct[val]

        #         if lo != 0 and first_value[lolo] == val:
        #             change[lolo][0] = change[hi][0]
        #             change[lolo][1] += change[hi][1]
        #             last_first[change[hi][0]] = lolo
        #         else:
        #             change[lo] = change[hi]
        #             last_first[change[hi][0]] = lo
        #             first_value[lo] = val
        #         change.pop(hi)
        #     elif lo != 0:
        #         dct[first_value[lolo]][lolo][0] = hi

        #     dct[k].pop(lo)
        #     return count ** 2

        # def dfs(dct, first_value, last_first, result):
        #     while dct:
        #         to_remove = []
        #         for k, v in dct.items():
        #             if len(v) == 1:
        #                 to_remove.append(k)
        #                 lo = next(iter(v.keys()))
        #                 result += remove(k, lo, dct, first_value, last_first)
        #         if to_remove:
        #             for k in to_remove:
        #                 dct.pop(k)
        #         else:
        #             break

        #     r = result
        #     for k, v in dct.items():
        #         for lo in v:
        #             if lo == 0 or v[lo][0] == n:
        #                 continue
        #             dct2 = deepcopy(dct)
        #             first_value2 = first_value.copy()
        #             last_first2 = last_first.copy()
        #             count = remove(k, lo, dct2, first_value2, last_first2)
        #             #dct2[k].pop(lo)
        #             r = max(
        #                 r, dfs(dct2, first_value2, last_first2, result+count))
        #     return r

        # return dfs(dct, first_value, last_first, 0)




assert Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
assert Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 2, 3, 1]) == 26
print(Solution().removeBoxes([8, 1, 2, 10, 8, 5, 1, 10, 8, 4]))
print(Solution().removeBoxes([3, 8, 8, 5, 5, 3, 9, 2, 4, 4, 6, 5, 8, 4, 8, 6, 9, 6, 2, 8, 6, 4, 1, 9, 5, 3, 10, 5, 3, 3, 9, 8, 8, 6, 5, 3, 7, 4, 9, 6, 3, 9, 4, 3, 5, 10, 7, 6, 10, 7]))
