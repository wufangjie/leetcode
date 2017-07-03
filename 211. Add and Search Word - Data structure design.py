from collections import defaultdict
from itertools import combinations

class WordDictionary(object):
    char = [chr(i) for i in range(97, 97+26)]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.data[len(word)].add(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        S = self.data[len(word)]
        if len(S) >= 26 ** word.count('.'):
            idx = [i for i, c in enumerate(word) if c == '.']
            if idx:
                word = list(word)
                for comb in combinations(self.char, len(idx)):
                    for i, c in zip(idx, comb):
                        word[i] = c
                    if ''.join(word) in S:
                        return True
            else:
                return word in S
        else:
            reg = re.compile(word)
            for w in S:
                if reg.match(w):
                    return True
        return False


    # ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]

    # [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))
print(wd.search("bad"))
print(wd.search(".ad"))
print(wd.search("b.."))
print(wd.search("dm"))




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
