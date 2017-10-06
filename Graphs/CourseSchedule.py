"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have 
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it 
possible for you to finish all courses?
"""

def makeGraph(arr):
    G = collections.defaultdict(list)
    for course, prereq in arr:
        G[prereq].append(course)
    return G

def topologicalSort(v, graph, done, process):
    if v in done: return False
    if v in process: return True
    process.add(v)
    for vertex in graph.get(v, []):
        if topologicalSort(vertex, graph, done, process): return True
    process.remove(v)
    done.add(v)
    return False

def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """   
    graph = makeGraph(prerequisites)
    done, process = set(), set()
    for vertex in graph:
        if topologicalSort(vertex, graph, done, process): return False
    return True