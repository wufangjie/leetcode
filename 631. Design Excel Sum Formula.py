from collections import defaultdict


class Excel(object):
    def __init__(self, H,W):
        """
        :type H: int
        :type W: str
        """
        self.excel = [[0] * (ord(W) - 64) for _ in range(H)]
        self.formula = {}
        self.graph = {}

    def _topo(self):
        rev = defaultdict(set)
        stack, count = [], {}
        for k, v in self.graph.items():
            for k2 in v:
                rev[k2].add(k)
            count[k] = len(v)
            if not v:
                stack.append(k)

        while stack:
            k = stack.pop()
            yield k
            for v in rev[k]:
                count[v] -= 1
                if count[v] == 0:
                    stack.append(v)

    def _update(self, rc, v):
        r, c = rc
        if v != self.excel[r][c]:
            add = {rc: v - self.excel[r][c]}
            for rc2 in self._topo():
                temp = sum(v * self.formula[rc2][k]
                           for k, v in add.items() if k in self.formula[rc2])
                if temp:
                    add[rc2] = temp

            for (i, j), v in add.items():
                self.excel[i][j] += v

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        rc = r - 1, ord(c) - 65
        if rc in self.formula:
            self.formula.pop(rc)
            self.graph.pop(rc)
            for f in self.graph.values(): # do not forget to discard
                f.discard(rc)
        self._update(rc, v)

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.excel[r - 1][ord(c) - 65]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        new_f = defaultdict(int)
        for s in strs:
            temp = s.split(':')
            r1, c1 = int(temp[0][1:]) - 1, ord(temp[0][0]) - 65
            if len(temp) == 1:
                new_f[r1, c1] += 1
            else:
                r2, c2 = int(temp[1][1:]) - 1, ord(temp[1][0]) - 65
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        new_f[i, j] += 1

        rc = r, c = int(r) - 1, ord(c) - 65
        if rc not in self.formula:
            for f, pre in self.formula.items():
                if rc in pre: # is pre not f
                    self.graph[f].add(rc)

        self.graph[rc] = set()
        for f in self.formula:
            if f in new_f:
                self.graph[rc].add(f)

        self.formula[rc] = new_f
        ret = sum(v * self.excel[i][j] for (i, j), v in new_f.items())
        self._update(rc, ret) # update rather than assignment
        return ret


from pprint import pprint

# obj = Excel(3, 'C')
# obj.set(1, "A", 2)
# pprint(obj.excel)
# obj.sum(3, "C", ["A1", "A1:B2"])
# pprint(obj.excel)
# obj.set(2, "B", 2)
# pprint(obj.excel)


# obj = Excel(26, 'Z')
# for op, p in zip(["set","set","sum","sum"], [[1,"A",1],[1,"I",1],[7,"D",["A1:D6","A1:G3","A1:C12"]],[10,"G",["A1:D7","D1:F10","D3:I8","I1:I9"]]]):
#     if op == 'set':
#         obj.set(*p)
#     elif op == 'sum':
#         obj.sum(*p)
#     else:
#         print('get', obj.get(*p))
#     print('---', op, p)
#     pprint(obj.excel)



# obj = Excel(5, 'E')
# for op, p in zip(["get","set","get","sum","set","get","sum","set","get"], [[1,"A"],[1,"A",1],[1,"A"],[2,"B",["A1","A1"]],[1,"A",2],[2,"B"],[3,"C",["B2","A1:B2"]],[2,"B",0],[3,"C"]]):
#     if op == 'set':
#         obj.set(*p)
#     elif op == 'sum':
#         obj.sum(*p)
#     else:
#         print('get', obj.get(*p))
#     print('---', op, p)
#     pprint(obj.excel)


obj = Excel(5, 'E')
for op, p in zip(["set","set","set","sum","get","set","get","sum","set","get","get","sum","set","get","get","get","get"], [[1,"A",5],[1,"B",3],[1,"C",2],[1,"C",["A1","A1:B1"]],[1,"C"],[1,"B",15],[1,"C"],[1,"B",["A1:A5"]],[5,"A",10],[1,"B"],[1,"C"],[3,"C",["A1:C1","A1:A5"]],[3,"A",3],[1,"B"],[1,"C"],[3,"C"],[5,"A"]]):
    if op == 'set':
        obj.set(*p)
    elif op == 'sum':
        obj.sum(*p)
    else:
        print('get', obj.get(*p))
    print('---', op, p)
    pprint(obj.excel)
