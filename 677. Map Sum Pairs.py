class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {'sum': 0}

    def search(self, key):
        node = self.trie
        for c in key:
            if c not in node:
                return 0
            node = node[c]
        return node.get('#', 0)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        add = val - self.search(key)
        node = self.trie
        for c in key:
            node['sum'] += add
            if c not in node:
                node[c] = {'sum': 0}
            node = node[c]
        node['sum'] += add
        node['#'] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return node['sum']



obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
print(obj.sum("app"))
print(obj.sum("appl"))
