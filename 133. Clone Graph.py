# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node

        node_dict = {node.label: UndirectedGraphNode(node.label)}
        Q = [node]
        while Q:
            current = Q.pop()
            for nd in current.neighbors:
                if nd.label not in node_dict:
                    node_dict[nd.label] = UndirectedGraphNode(nd.label)
                    Q.append(nd)
                node_dict[current.label].neighbors.append(node_dict[nd.label])
        return node_dict[node.label]
