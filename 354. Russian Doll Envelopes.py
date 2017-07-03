import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes = sorted(envelopes)

        res, dct = [], {}
        inf = float('inf')
        pre = -inf
        for w, h in envelopes:
            if w > pre:
                if len(res) in dct:
                    res.append(0)
                for k, v in dct.items():
                    res[k] = v
                pre = w
                dct = {}
            i = bisect.bisect_left(res, h)
            dct[i] = min(h, dct.get(i, inf))

        n = len(res)
        return n + (n in dct)


print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))


# inspired by 300. Longest Increasing Subsequence.py
