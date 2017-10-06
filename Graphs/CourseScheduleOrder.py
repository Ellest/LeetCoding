"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have 
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return 
the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. 
If it is impossible to finish all courses, return an empty array.
"""

def makeGraph(prereqs, connected):
    graph = collections.defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        if prereq in connected: connected.remove(prereq)
        if course in connected: connected.remove(course)
    return graph
    
def topSort(v, graph, done, process, order):
    if v in done: return False
    if v in process: return True
    process.add(v)
    for vertex in graph.get(v, []):
        if topSort(vertex, graph, done, process, order): return True
    process.remove(v)
    done.add(v)
    order.appendleft(v)
    return False

def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """    
    connected = set(range(numCourses))
    graph = makeGraph(prerequisites, connected)
    courseOrder = collections.deque(list(connected))
    done, process = set(), set()
    for vertex in graph:
        if topSort(vertex, graph, done, process, courseOrder): return []
    return list(courseOrder)