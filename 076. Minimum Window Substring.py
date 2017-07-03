from collections import deque, Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dct = Counter(t)
        count = len(t)
        current = {k: deque([], maxlen=v) for k, v in dct.items()}
        start = -1
        best = (float('inf'), 0, -1)
        for i, c in enumerate(s):
            if c in dct:
                if len(current[c]) < dct[c]:
                    count -= 1

                re_cal = (True if count == 0
                          and (start < 0 or current[c][0] == start) else False)

                current[c].append(i)
                if re_cal:
                    start = min(v[0] for v in current.values())
                    if i - start < best[0]:
                        best = (i - start, start, i)

        return s[best[1] : best[2]+1]



print(Solution().minWindow("ADOBECODEBANC", "ABC"))
