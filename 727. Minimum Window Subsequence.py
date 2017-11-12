from collections import defaultdict


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        pre = defaultdict(list)
        for i, c in enumerate(T, -1):
            pre[c].append(i)
        for val in pre.values():
            val.reverse()

        start_index = [None] * (len(T) + 1)
        lo, hi = float('-inf'), 0
        for i, c in enumerate(S):
            start_index[-1] = i
            for p in pre[c]:
                if start_index[p] is not None:
                    start_index[p + 1] = start_index[p]
            if (c == T[-1] and start_index[-2] is not None
                and i - start_index[-2] < hi - lo):
                lo, hi = start_index[-2], i
        if lo < 0:
            return ''
        else:
            return S[lo:hi+1]

# print(Solution().minWindow("abcdebdde", "bde"))
# print(Solution().minWindow("nkzcnhczmccqouqadqtmjjzltgdzthm", "bt"))
print(Solution().minWindow("cnhczmccqouqadqtmjjzl", "mm"))
