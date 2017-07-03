from collections import defaultdict


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        words = sorted(words, key=len, reverse=True)
        word_len = list(map(len, words))
        set_list = [set(w) for w in words]

        stats = defaultdict(set)
        for i, s in enumerate(set_list):
            for c in s:
                stats[c].add(i)

        max_second_len = 0
        theMax = 0
        for i, w1 in enumerate(words):
            if word_len[i] <= max_second_len:
                break

            left = set(range(n))
            for c in set_list[i]:
                left.difference_update(stats[c])

            if left:
                j = sorted(left)[0]
                theMax = max(theMax, word_len[i] * word_len[j])
                max_second_len = max(max_second_len, word_len[j])
        return theMax


print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
