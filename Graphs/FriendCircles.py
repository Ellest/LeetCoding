"""

There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, 
and B is a direct friend of C, then A is an indirect friend of C. And we defined a 
friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the 
class. If M[i][j] = 1, then the ith and jth students are direct friends with each other
, otherwise not. And you have to output the total number of friend circles among all 
the students.

"""


"""
#
# DFS approach in finding connected components (groups)
#
"""
def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    circles = 0
    visited = set()
    for i in range(len(M)):
        if i not in visited:
            circles += 1 # increment count
            stack = [i] # create stack and initialize it with starting person
            visited.add(i)
            while stack:
                row = stack.pop() # next row to process
                for j in range(len(M[row])):
                    if j != i and M[row][j] and j not in visited:
                        visited.add(j)
                        stack.append(j) 
    return circles