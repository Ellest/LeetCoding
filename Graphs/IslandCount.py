"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def mark(rcPair, m, n, grid, visited, directions):
    visited.add(rcPair)
    queue = collections.deque([rcPair])
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nxtR, nxtC = row + dr, col + dc
            pair = (nxtR, nxtC)
            if 0 <= nxtR < n and 0 <= nxtC < m and grid[nxtR][nxtC] == '1' and pair not in visited:
                visited.add(pair)
                queue.append(pair)

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """    
    cnt = 0
    visited = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            pair = (r,c)
            if grid[r][c] == '1' and pair not in visited:
                cnt += 1
                mark(pair, len(grid[0]), len(grid), grid, visited, directions)
    return cnt