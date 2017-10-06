"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board: return
    l, h = len(board[0]), len(board)
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    touchQueue = collections.deque()

    # Enqueuing border O's and marking with a token
    for r in (0, h-1):
        for c in range(l):
            if board[r][c] == 'O':
                touchQueue.append((r,c))
                board[r][c] = 'T'
    for c in (0, l-1):
        for r in range(1, h-1):
            if board[r][c] == 'O':
                touchQueue.append((r,c))
                board[r][c] = 'T'

    # iterative BFS to mark unenclosed regions
    while touchQueue:
        r, c = touchQueue.popleft()
        for dr, dc in directions:
            nxtR, nxtC = r + dr, c + dc
            if 0 <= nxtR < h and 0 <= nxtC < l and board[nxtR][nxtC] == 'O':
                board[nxtR][nxtC] = 'T'
                touchQueue.append((nxtR,nxtC))

    # iterate through board to flip 
    for r in range(h):
        for c in range(l):
            if board[r][c] == 'T':
                board[r][c] = 'O'
            elif board[r][c] == 'O':
                board[r][c] = 'X'