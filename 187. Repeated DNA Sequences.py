class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        more_than_once, once = set(), set()
        for i in range(len(s) - 9):
            t = s[i:i+10]
            if t not in more_than_once:
                if t in once:
                    more_than_once.add(t)
                else:
                    once.add(t)
        return list(more_than_once)

        # if overlap is not permit
        # more_than_once, once = {}, {}
        # for i in range(len(s) - 9):
        #     t = s[i:i+10]
        #     if t not in more_than_once:
        #         if t in once:
        #             more_than_once[t] = [once[t], i]
        #         else:
        #             once[t] = i
        #     else:
        #         more_than_once[t][1] = i
        # return list(k for k, v in more_than_once.items() if v[1] - v[0] >= 10)

if __name__ == '__main__':
    assert sorted(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == ['AAAAACCCCC', 'CCCCCAAAAA']
    assert Solution().findRepeatedDnaSequences('AAAAAAAAAAA') == ['AAAAAAAAAA']
    # assert Solution().findRepeatedDnaSequences('AAAAAAAAAAAAAAAAAAAA') == ['AAAAAAAAAA']
