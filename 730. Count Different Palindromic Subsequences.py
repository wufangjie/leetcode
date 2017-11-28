from utils import memo
# from collections import defaultdict
# import bisect



class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        @memo
        def dfs(lo, hi):
            if lo >= hi:
                return 0
            elif lo == hi - 1:
                return 1
            elif lo == hi - 2:
                return 2
            ret = 0
            for c in 'abcd':
                i = S.find(c, lo, hi)
                if i != -1:
                    j = S.rfind(c, i, hi)
                    if i == j:
                        ret += 1
                    else:
                        ret += 2 + dfs(i + 1, j)
                        # this 2 means midst 1 or 2 element c
            return ret % 1000000007
        return dfs(0, len(S))


        # # TLE 366/366
        # dct = defaultdict(list)
        # for i, c in enumerate(S):
        #     dct[c].append(i)

        # @memo
        # def dfs(lo, hi):
        #     if lo > hi:
        #         return 0
        #     elif lo == hi:
        #         return 1
        #     elif lo == hi - 1:
        #         return 2
        #     ret = 0
        #     for c in 'abcd':
        #         i = bisect.bisect_left(dct[c], lo)
        #         j = bisect.bisect_right(dct[c], hi, lo=i) - 1
        #         if i < j:
        #             ret += 2 + dfs(dct[c][i] + 1, dct[c][j] - 1)
        #             # this 2 means midst 1 or 2 element c
        #         elif i == j:
        #             ret += 1
        #     return ret
        # return dfs(0, len(S) - 1) % 1000000007


print(Solution().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'), 3104860382)


import time
tic = time.time()
print(Solution().countPalindromicSubsequences("dacacddcdbdbcdbcbdaacbbdddbdbaabddaacdabcbaabadaaccdcddabcadacbcdabdaaccdbccbbccaabcbcbbdcccadababbddadbabcbdbddacccccbbcbbadbacaaccbbbaddcdbcacbaabbdbdbdbbadbcadbcadbcdbbaaadcddddddadacbacddcadbcbbddcacaddacddcbabdaddbbbdcdaaacdadabdbaabbbbadbccdbdbcbacbdcdddcbabdaabaddddabbbdcadccddcacccbabcbdcdabaabcccbbacadccbbbaabcababaccaaacddbcaaaacbbbbbdbbcacacbcaadadabdccbdbcbdbbbccbddabccbacaabacdddbccdddbdaacacdabaddbcacbaddbabcbaaddabdaddccadcdaacbadbcdccbaddbdabdbbddaccddadacdadcddacbbbbbcccbcaacabdabcbccdacbbdbaccaccadcdbcbccdcabbdaaacabdcadabbabdaadaaadcccddbabaccbddcddcbccdbbadaaaaaabbdccccadbacdadcaaacdcbbcbbcaadcccbabcddbdacbbcbbcaddabaabbcccdbccdbcabadbbbdcbcacdbadcadadddaabcdcddcdcaabaacbaccdacdaddcbdbdddaaccbbcdacaddaabbcdaabccbcdbccbbbaaaabdbabdcabbddcadcbadbbaccccbbccaadccbcdbabaaddcababbcccdabbdbaddbbccaaacdbbcdbdbcdaaacaaabccbdbcbabaadbcddaccaadccbcaacbbbaddadbabccacaccddababcdbdbadbbdcaadadbaccbbaddcdabadbbbdcabdccaadadbcbadccadabcdaadbabaabddcdbbcccabdccbbdcdbbbbbabdbbdbaaadb"))
print(time.time() - tic)
