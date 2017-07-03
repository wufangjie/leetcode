class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        _dict = self._dict
        for w in word:
            if w not in _dict:
                _dict[w] = {}
            _dict = _dict[w]
        _dict[''] = ''

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        _dict = self._dict
        for w in word:
            if w not in _dict:
                return False
            _dict = _dict[w]
        return '' in _dict


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        _dict = self._dict
        for w in prefix:
            if w not in _dict:
                return False
            _dict = _dict[w]
        return True

# usually use '#' instead of ''

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
obj.insert('app')
print(obj.search('app'))
print(obj.search('appl'))
print(obj.search('applee'))

print(obj.startsWith('ap'))

# param_3 = obj.startsWith(prefix)
