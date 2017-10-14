from collections import Counter
from heapq import nsmallest


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return [word for _, word in nsmallest(
            k, ((-v, w) for w, v in Counter(words).items()))]


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
