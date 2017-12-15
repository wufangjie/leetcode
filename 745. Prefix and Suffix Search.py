from utils import memo
import bisect


class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.n = len(words)
        self.words = words
        self.seq_w = sorted(range(self.n), key=lambda i: words[i])
        self.seq = [words[i] for i in self.seq_w]
        words_rev = [w[::-1] for w in words]
        self.rev_w = sorted(range(self.n), key=lambda i: words_rev[i])
        self.rev = [words_rev[i] for i in self.rev_w]

    @memo
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if prefix:
            lo_p = bisect.bisect_left(self.seq, prefix)
            hi_p = bisect.bisect_left(self.seq, prefix + '{', lo=lo_p)
        else:
            lo_p, hi_p = 0, self.n

        if suffix:
            temp = suffix[::-1]
            lo_s = bisect.bisect_left(self.rev, temp)
            hi_s = bisect.bisect_left(self.rev, temp + '{', lo=lo_s)
        else:
            lo_s, hi_s = 0, self.n

        weight = -1
        if hi_p - lo_p > hi_s - lo_s:
            for i in range(lo_s, hi_s):
                if self.words[self.rev_w[i]].startswith(prefix):
                    if self.rev_w[i] > weight:
                        weight = self.rev_w[i]
        else:
            for i in range(lo_p, hi_p):
                if self.seq[i].endswith(suffix):
                    if self.seq_w[i] > weight:
                        weight = self.seq_w[i]
        return weight



# NOTE: words=[apple], prefix='appl', suffix='le' if valid
# NOTE: TLE 7/12 when I did not add memo, though I think it may not be the correct way

import time
tic = time.time()
obj = WordFilter(["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])

for p, s in [["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]:
    print(obj.f(p, s))
print(time.time() - tic)
