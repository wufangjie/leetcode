class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # # 298ms, NOTE: with those test cases, balance is useless
        # if len(words1) != len(words2):
        #     return False

        # self.disjoint = {}
        # count = {}
        # for a, b in pairs:
        #     if a not in self.disjoint:
        #         self.disjoint[a] = a
        #         count[a] = 1
        #     if b not in self.disjoint:
        #         self.disjoint[b] = b
        #         count[b] = 1

        #     pa, pb = self.get_parent(a), self.get_parent(b)
        #     if count[pa] > count[pb]:
        #         self.disjoint[pb] = pa
        #         count[pa] += count[pb]
        #     else:
        #         self.disjoint[pa] = pb
        #         count[pb] += count[pa]

        # for w1, w2 in zip(words1, words2):
        #     if w1 != w2:
        #         if (w1 not in self.disjoint
        #             or w2 not in self.disjoint
        #             or (self.get_parent(w1) != self.get_parent(w2))):
        #             return False
        # return True


        # 249ms
        if len(words1) != len(words2):
            return False

        self.disjoint = {}
        for a, b in pairs:
            if a not in self.disjoint:
                self.disjoint[a] = b
                if b not in self.disjoint:
                    self.disjoint[b] = b
            elif b not in self.disjoint:
                self.disjoint[b] = a
            else:
                pa, pb = self.get_parent(a), self.get_parent(b)
                self.disjoint[pa] = pb

        for w1, w2 in zip(words1, words2):
            if w1 != w2:
                if (w1 not in self.disjoint
                    or w2 not in self.disjoint
                    or (self.get_parent(w1) != self.get_parent(w2))):
                    return False
        return True

    def get_parent(self, w):
        if self.disjoint[w] != w:
            self.disjoint[w] = self.get_parent(self.disjoint[w])
        return self.disjoint[w]



print(Solution().areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]))
