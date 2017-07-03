class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        idx, seq = [], []
        for i, elem in enumerate(s):
            if elem in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                idx.append(i)
                seq.append(elem)
        for i, elem in zip(idx, seq[::-1]):
            result[i] = elem
        return ''.join(result)

assert Solution().reverseVowels("helloOaeiu") == "hullieaOoe"
