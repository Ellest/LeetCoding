"""
Given an m x n matrix of non-negative integers representing 
the height of each unit cell in a continent, the "Pacific ocean" touches 
the left and top edges of the matrix and the "Atlantic ocean" touches the 
right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a 
cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific 
and Atlantic ocean.
"""


def pacificAtlantic(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    
    if not matrix: return []
    length, height = len(matrix[0]), len(matrix)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # set up BFS from pacific end
    pacific = [(0, i) for i in range(length)] + [(i, 0) for i in range(1, height)]
    pQueue = collections.deque(pacific)
    pacificSet = set(pacific)
    
    # iterative BFS using queue
    while pQueue:
        r, c = pQueue.popleft()
        for dr, dc in directions:
            R, C = r + dr, c + dc
            if 0 <= R < height and 0 <= C < length:
                coord = (R, C)
                if coord not in pacificSet and matrix[r][c] <= matrix[R][C]:
                    pacificSet.add(coord)
                    pQueue.append(coord)
                    
    # setting up BFS from atlantic end
    atlantic = [(height-1, i) for i in range(length)] + [(i, length-1) for i in range(height-1)]
    aQueue = collections.deque(atlantic)
    atlanticSet = set(atlantic)
    result_set = []
    
    # iterative BFS using queue
    while aQueue:
        coord = aQueue.popleft()
        r,c = coord
        if coord in pacificSet: 
            result_set.append([r,c])
        for dr, dc in directions:
            R, C = r + dr, c + dc
            if 0 <= R < height and 0 <= C < length:
                coord = (R, C)
                if coord not in atlanticSet and matrix[r][c] <= matrix[R][C]:
                    atlanticSet.add(coord)
                    aQueue.append(coord)
    return result_set