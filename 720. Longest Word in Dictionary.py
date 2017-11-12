class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key=len)
        pre, pre2 = set(), {''}
        max_len = 1
        for w in words:
            # print(pre, pre2)
            lw = len(w)
            if lw > max_len:
                break
            elif lw == max_len:
                if not pre2:
                    break
                max_len += 1
                pre, pre2 = pre2, pre
                pre2.clear()

            if w[:-1] in pre:
                pre2.add(w)

        if pre2:
            return min(pre2)
        else:
            return min(pre)


#print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(Solution().longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))
