from collections import defaultdict


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        dct = defaultdict(set)
        count = 0
        for w1, w2 in zip(words1, words2):
            if w1 != w2:
                if w2 not in dct[w1]:
                    dct[w1].add(w2)
                    count += 1
        if count == 0:
            return True

        for w1, w2 in pairs:
            if w1 in dct and w2 in dct[w1]:
                dct[w1].remove(w2)
                count -= 1
                if count == 0:
                    return True
            if w2 in dct and w1 in dct[w2]:
                dct[w2].remove(w1)
                count -= 1
                if count == 0:
                    return True
        return False


print(Solution().areSentencesSimilar(
    ["great","acting","skills"],
    ["fine","drama","talent"],
    [["great","fine"],["drama","acting"],["skills","talent"]]))
