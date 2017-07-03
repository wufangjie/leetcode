from collections import Counter, deque


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0 # not k or k + 1
        for key, total in sorted(Counter(s).items(), key=lambda x: -x[1]):
            if total + k <= longest:
                break
            Q = deque([-1], maxlen=k+2)
            for i, c in enumerate(s):
                if c != key:
                    if len(Q) == k + 2:
                        longest = max(longest, Q[-1] - 1 - Q[0])
                        total -= Q[1] - Q[0] - 1
                        if total + k <= longest:
                            break
                    Q.append(i)
            else:
                if len(Q) < k + 2:
                    Q.extendleft([-1] * (k + 2 - len(Q)))
                longest = max(longest, Q[-1] - 1 - Q[0], i - Q[1])
        return longest

assert Solution().characterReplacement("ABAB", 2) == 4
assert Solution().characterReplacement("AABA", 0) == 2
assert Solution().characterReplacement("BAAAB", 2) == 5
assert Solution().characterReplacement("", 0) == 0
assert Solution().characterReplacement("", 2) == 0


#'fasdfsadfsdfasfsdfsdfsdfsadfsdfsdfasdfsdfasdfsfgasdfdasd'
