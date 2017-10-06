"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

def updateMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = collections.deque()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if not matrix[r][c]:
                queue.append((r,c))
                matrix[r][c] = 0
            else:
                matrix[r][c] = float('inf')
    
    if not matrix: return 
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    lv = 0
    l, h = len(matrix[0]), len(matrix)
    while queue:
        nxtLV = lv + 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nxtR, nxtC = r + dr, c + dc
                if 0 <= nxtR < h and 0 <= nxtC < l and matrix[nxtR][nxtC] > nxtLV:
                    matrix[nxtR][nxtC] = nxtLV
                    queue.append((nxtR, nxtC))
        lv += 1
    return matrix