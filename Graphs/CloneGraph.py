"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

def cloneGraph(node):
    if not node: return
    returnNode = UndirectedGraphNode(node.label)
    stack = [node]
    _map = {node : returnNode}
    while stack:
        current = stack.pop()
        for n in current.neighbors:
            if n in _map:
                _map[current].neighbors.append(_map[n])
            else:
                temp = UndirectedGraphNode(n.label)
                _map[n] = temp
                _map[current].neighbors.append(temp)
                stack.append(n)
    return returnNode