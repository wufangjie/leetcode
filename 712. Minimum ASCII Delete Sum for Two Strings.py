from collections import defaultdict



class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1, s2 = [ord(c) for c in s1], [ord(c) for c in s2]
        n1, n2 = len(s1), len(s2)

        dct = defaultdict(list)
        for i, elem in enumerate(s2, 1):
            dct[elem].append(i)

        for val in dct.values():
            val.reverse()

        dp = [0] * (n2 + 1) + [float('inf')]

        for elem in s1:
            for pos in dct[elem]:
                if dp[pos] < dp[pos - 1] + elem:
                    dp[pos] = dp[pos - 1] + elem
                    while dp[pos + 1] < dp[pos]:
                        dp[pos + 1] = dp[pos]
                        pos += 1
        return sum(s1) + sum(s2) - 2 * dp[-2]


        # # later1 = [{}]
        # # for i in range(n1 - 1, 0, -1):
        # #     later1.append(later1[-1].copy())
        # #     later1[-1][s1[i]] = i
        # # later1.reverse()

        # later2 = [{}]
        # for i in range(n2 - 1, 0, -1):
        #     later2.append(later2[-1].copy())
        #     later2[-1][s2[i]] = i
        # later2.reverse()

        # _cache = {}

        # def dfs(i, j):
        #     if i == n1:
        #         return sum(s2[j:])
        #     elif j == n2:
        #         return sum(s1[i:])
        #     if (i, j) in _cache:
        #         return _cache[i, j]
        #     if s1[i] == s2[j]:
        #         _cache[i, j] = temp = dfs(i + 1, j + 1)
        #         return temp

        #     next_j = later2[j].get(s1[i], 0)
        #     ret = s1[i] + dfs(i + 1, j)
        #     if next_j:
        #         ret = min(ret, dfs(i + 1, next_j) + sum(s2[j:next_j]))
        #     return ret

        #     # if s1[i] not in later2[j]:
        #     #     _cache[i, j] = temp = s1[i] + dfs(i + 1, j)
        #     #     return temp
        #     # elif s2[j] not in later1[i]:
        #     #     _cache[i, j] = temp = s2[j] + dfs(i, j + 1)
        #     #     return temp
        #     # _cache[i, j] = temp = min(s1[i] + dfs(i + 1, j), s2[j] + dfs(i, j + 1))
        #     # return temp
        # return dfs(0, 0)


        # # TLE 81/94
        # s1, s2 = [ord(c) for c in s1], [ord(c) for c in s2]
        # n1, n2 = len(s1), len(s2)

        # @memo
        # def dfs(i, j):
        #     if i == n1:
        #         return sum(s2[j:])
        #     elif j == n2:
        #         return sum(s1[i:])
        #     if s1[i] == s2[j]:
        #         return dfs(i + 1, j + 1)
        #     return min(s1[i] + dfs(i + 1, j), s2[j] + dfs(i, j + 1))
        # return dfs(0, 0)



print(Solution().minimumDeleteSum("sea", "eat"))
print(Solution().minimumDeleteSum("ccaccjp", "fwosarcwge"))
print(Solution().minimumDeleteSum("owlqodgjymqjdnzmqkpibgzgmrcuyeqkjxyrvpjsodowankqujfilsiqkpsdstfviinfcxgqfcktapoxugmazmeteiombygnwscxyjocfdmbgwyvmxqyejpdxuzzvrjqwqydynfqabqnoxgmawjgkromokjplkdwncbyskzpauvvbvsvresvutwceogrfasykqkxwbygvgefyobvffqehadjwpmjouhdvvapyftdebntqbdqefvqchjtrohzxwhnjwpvgxktfm",
"aytzrhuypsgcepvzhwdzrqunymvigazwatrbhxbuyjvqijrftzxlmygrtujeavjlsdamcbocdksisqjkqglqubqzytchaaykcckmpapurbdjcityivlgtvwbhjzxibrxcjmcyldvbkitqjhmfslljvecdbujcckswnikjvvpevxbaburcaredzlwqlikbwaighvyfkpylxudojniymbbaijxqmshavqrxmeluoninvexjqnxpaxjnnclacgbuezlyqpjughbeqgphqvdggxtdnoewvnxbhuercyqxudtiobobrnuzfxdqctkhojomssoqilayabykfhxgzvfcpmtxcveykoxnoxdkkqtlszyyhs"))
