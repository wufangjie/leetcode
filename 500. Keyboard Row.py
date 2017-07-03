row = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for w in words:
            pre = None
            for c in w:
                i = ord(c)
                i = i - 97 if i > 96 else i - 65
                if pre is None:
                    pre = row[i]
                elif row[i] != pre:
                    break
            else:
                result.append(w)
        return result
