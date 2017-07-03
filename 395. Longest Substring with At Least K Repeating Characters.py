from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def rec(lo, hi, current_max):
            if hi - lo <= current_max:
                return current_max
            count = Counter(s[lo:hi])
            split = {key for key, val in count.items() if val < k}
            if split:
                theMax, start = 0, lo - 1
                for i in range(lo, hi):
                    if s[i] in split:
                        theMax = rec(start + 1, i, theMax)
                        start = i
                theMax = rec(start + 1, hi, theMax)
                return theMax
            else:
                return hi - lo

        return rec(0, len(s), 0)


        # def rec(lo, hi):
        #     if lo >= hi:
        #         return 0
        #     count = Counter(s[lo:hi])
        #     split = {key for key, val in count.items() if val < k}
        #     if split:
        #         theMax, start = 0, lo - 1
        #         for i in range(lo, hi):
        #             if s[i] in split:
        #                 theMax = max(theMax, rec(start + 1, i))
        #                 start = i
        #         theMax = max(theMax, rec(start + 1, hi))
        #         return theMax
        #     else:
        #         return hi - lo

        return rec(0, len(s))


print(Solution().longestSubstring("ababbcdc", 2))
