class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        td = {}
        for f, t in tickets:
            if f not in td:
                td[f] = {}
            if t in td[f]:
                td[f][t] += 1
            else:
                td[f][t] = 1


        def dfs_can_back(p, t, visited):
            if p == t:
                return True
            visited.add(p)
            for q in td.get(p, []):
                if q not in visited and dfs_can_back(q, t, visited):
                    return True
            return False


        key = 'JFK'
        result = [key]
        while key in td:
            poss = sorted(td[key].keys())
            if len(poss) == 1:
                p = poss[0]
                td[key][p] -= 1
                if td[key][p] == 0:
                    td.pop(key)
            else:
                for p in poss:
                    if dfs_can_back(p, key, set()):
                        td[key][p] -= 1
                        if td[key][p] == 0:
                            td[key].pop(p)
                        break
            result.append(p)
            key = p
        return result

# 题目的意思是要全部用上
assert Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
assert Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
assert Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ['JFK', 'NRT', 'JFK', 'KUL']
assert Solution().findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]) == ['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'ANU', 'TIA', 'JFK']
assert Solution().findItinerary([["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]) == ["JFK","ANU","EZE","AXA","TIA","AUA","EZE","JFK","ANU","EZE","TIA","JFK","AUA"]
