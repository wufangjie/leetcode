from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dct = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                dct[email].append(i)

        n = len(accounts)
        self.disjoint = list(range(n))
        for v in dct.values():
            p0 = self.find(v[0])
            for v2 in v[1:]:
                self.update(v2, p0)

        for i in range(n):
            self.flat(i)

        ret = [None] * n
        for i, p in enumerate(self.disjoint):
            if ret[p] is None:
                ret[p] = [accounts[i][0], set(accounts[i][1:])]
            else:
                ret[p][1].update(set(accounts[i][1:]))

        return [account[:1] + sorted(account[1])
                for account in ret if account is not None]

    def update(self, i, j):
        if self.disjoint[i] != i:
            self.update(self.disjoint[i], j)
        self.disjoint[i] = j

    def find(self, i):
        if self.disjoint[i] != i:
            return self.find(self.disjoint[i])
        return i

    def flat(self, i):
        if self.disjoint[i] == i:
            return i
        self.disjoint[i] = self.flat(self.disjoint[i])
        return self.disjoint[i]


# print(Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))

print(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
