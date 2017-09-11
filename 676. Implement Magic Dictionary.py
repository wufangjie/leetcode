class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        nodes = [None] * (n - 1) + [self.trie]
        for i in range(n):
            node = nodes[i - 1]
            if not node:
                break

            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c in node:
                    if c == word[i]:
                        nodes[i] = node[c]
                    else:
                        node2 = node[c]
                        for j in range(i + 1, n):
                            if word[j] not in node2:
                                break
                            node2 = node2[word[j]]
                        else:
                            if '#' in node2:
                                return True
        return False





# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello","leetcode"])
for word in ["hello", "hhllo", "hell", "leetcoded"]:
    print(obj.search(word))

# param_2 = obj.search(word)
