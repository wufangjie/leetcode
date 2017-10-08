from utils import memo
from collections import Counter


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        count = Counter(target)
        target = tuple(count.values())
        choices = {tuple(word.count(c, 0) for c in count) for word in stickers}
        count_nonzero = [0] * len(target)
        for ch in choices:
            single = 1
            for i, c in enumerate(ch):
                if c != 0:
                    count_nonzero[i] += 1
                if c < target[i]:
                    single = 0
            if single:
                return 1

        seq = sorted(range(len(count_nonzero)), key=lambda x: count_nonzero[x])
        # order is important
        if count_nonzero[seq[0]] == 0:
            return -1

        @memo
        def dfs(target):
            for i in seq:
                if target[i] > 0:
                    break
            else:
                return 0
            return min(1 + dfs(tuple(max(t - c, 0) for c, t in zip(ch, target)))
                       for ch in choices if ch[i] > 0)
        return dfs(target)



print(Solution().minStickers(["with", "example", "science"], "thehat"))
print(Solution().minStickers(["notice", "possible"], "basicbasic"))
print(Solution().minStickers(["seven","old","stream","century","energy","period","an","proper","together","sight","carry","milk","appear","winter","field","rather","caught","danger","lake","shall","machine","few","other","test","got","wing","map","finish","though","observe","log","they","foot","path","eat","glad","must","bar","did","of","clear","work","rule","quotient","produce","clean","wild","grass","example","left"], "weresurprise"))
print(Solution().minStickers(["among","own","apple","is","crop","general","shape","set","human","milk","select","fill","sell","again","death","dictionary","provide","opposite","lake","sugar","take","east","until","nose","division","begin","fish","though","big","felt","sight","dark","famous","market","rest","broke","half","ask","throw","arrange","like","language","these","region","dog","against","turn","length","can","could"], "pluralmark"))
