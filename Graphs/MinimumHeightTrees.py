"""
For a undirected graph with tree characteristics, we can choose any node as the
root. The result graph is then a rooted tree. Among all possible rooted trees, 
those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given 
the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are 
undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""
def make_graph(edges):
    graph = collections.defaultdict(list)
    for one, two in edges:
        graph[one].append(two)
        graph[two].append(one)
    return graph

def findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    
    if not edges: return [0] if n else []
    graph = make_graph(edges)
    # pick a random node
    start = graph.keys()[0]

    # first bfs to find furthest node from start node
    queue = collections.deque([start])
    visited = set([start])
    furthest = None
    while queue:
        vertex = queue.popleft()
        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                furthest = v

    # find furthest node from furthest node
    queue = collections.deque([furthest])
    parents = {furthest:None}
    end = None
    length = 0
    while queue:
        for _ in range(len(queue)):
            vertex = queue.popleft()
            for v in graph[vertex]:
                if v not in parents:
                    parents[v] = vertex
                    queue.append(v)
                    end = v
        length += 1

    # get number of edges until root
    half = (length-1) // 2 
    while half:
        end, half = parents[end], half - 1
    return [end] if length % 2 else [end, parents[end]]