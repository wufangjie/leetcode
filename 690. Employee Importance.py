"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dct = {p.id: p for p in employees}
        if id not in dct:
            return 0
        p = dct[id]
        ret = p.importance
        stack = p.subordinates[:]
        while stack:
            p = dct.get(stack.pop())
            if p:
                ret += p.importance
                stack.extend(p.subordinates)
        return ret
