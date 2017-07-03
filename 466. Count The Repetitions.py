# from collections import Counter
# from utils import memo


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0

        l1, l2 = len(s1), len(s2)
        # theMin = min(Counter(s2).values())
        # for i in range(theMin, 1, -1):
        #     if i % theMin == 0:
        #         p = l2 // i
        #         if s2[:p] * i == s2:
        #             s2 = s2[:p]
        #             l2 = p
        #             n2 *= i
        #             break

        # @memo
        def match(i):
            count = j = 0
            while j < l1:
                if s1[j] == s2[i]:
                    i += 1
                    if i == l2:
                        count += 1
                        i = 0
                j += 1
            return count, i

        i = 0
        count = [0]
        visited = {0: 0}
        for j in range(1, n1 + 1):
            temp, i = match(i)
            count.append(count[-1] + temp)
            if i in visited:
                break
            visited[i] = j

        j = visited[i]
        n1 -= j
        pre = count[j]
        count = [0] + [c - pre for c in count[j+1:]]
        lc = len(count) - 1
        return (pre + count[-1] * n1 // lc + count[n1 % lc]) // n2


print(Solution().getMaxRepetitions("acb", 4, "ab", 2))
print(Solution().getMaxRepetitions("abcdefg", 100, "gfedcba", 3))
print(Solution().getMaxRepetitions("aahumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxf", 1000000, "aac", 1000000))
print(Solution().getMaxRepetitions("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikef", 1000000, "fmznimkkasvwsrenzkycxfxtlsgypsfad", 333))
