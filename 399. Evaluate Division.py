class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        value_dict, count = {}, {}

        def get_unit(p):
            if value_dict[p][1] == p:
                return value_dict[p]
            else:
                v, q = value_dict[p]
                v2, q2 = get_unit(q)
                value_dict[p] = (v * v2, q2)
                return value_dict[p]

        for (a, b), v in zip(equations, values):
            if a in value_dict:
                if b not in value_dict:
                    v2, a2 = get_unit(a)
                    value_dict[b] = (v2 / v, a2)
                    count[a2] += 1
                else:
                    va, a2 = get_unit(a)
                    vb, b2 = get_unit(b)
                    if count[a2] < count[b2]:
                        value_dict[a2] = (v * vb / va, b2)
                        count[b2] += count[a2]
                        count.pop(a2)
                    else:
                        value_dict[b2] = (va / v / vb, a2)
                        count[a2] += count[b2]
                        count.pop(b2)
            else:
                if b in value_dict:
                    v2, b2 = get_unit(b)
                    value_dict[a] = (v * v2, b2)
                    count[b2] += 1
                else:
                    value_dict[a] = (v, b)
                    value_dict[b] = (1.0, b)
                    count[b] = 2

        result = []
        for a, b in queries:
            if a not in value_dict or b not in value_dict:
                result.append(-1.0)
            else:
                va, a2 = get_unit(a)
                vb, b2 = get_unit(b)
                if a2 != b2:
                    result.append(-1.0)
                else:
                    result.append(va / vb)
        return result


print(Solution().calcEquation([["a","b"],["e","f"],["b","e"]],
                        [3.4,1.4,2.3],
                        [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
