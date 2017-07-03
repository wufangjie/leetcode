class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        maxlen = len(s)

        matched_before_position = {}
        matched_before_position[0] = 0

        for i in range(1, maxlen+1):
            possible = set()
            for j in matched_before_position:
                if s[j:i] in wordSet:
                        possible.add(j)
            if possible:
                matched_before_position[i] = possible

        def get_results(lastCut, result, results):
            if lastCut == 0:
                results.append(' '.join(map(lambda x: s[x[0] : x[1]],
                                            zip(result[:-1], result[1:]))))
            else:
                for preCut in matched_before_position[lastCut]:
                    get_results(preCut, [preCut] + result, results)

        results = []
        if maxlen in matched_before_position:
            get_results(maxlen, [maxlen], results)
        return results



if __name__ == '__main__':
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # 在最后要输出的时候再组合, 否则可能做无用功, TLE
    print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
