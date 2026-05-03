"""
LeetCode 130 - Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Pattern:
Graph Traversal (DFS/BFS) on Matrix
"""
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        M, N = len(board), len(board[0])
        def dfs(i: int, j: int):
            nonlocal dirs, M, N
            st = [(i, j)]
            board[i][j] = 'T'
            while st:
                x, y = st.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < M and 0 <= ny < N):
                        continue
                    if board[nx][ny] == 'O':
                        board[nx][ny] = 'T'
                        st.append((nx, ny))
        for i in [0, M-1]:
            for j in range(N):
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(1, M-1):
            for j in [0, N-1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
      

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" ".join(row))
    print()

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print_board(board)
sol.solve(board)
print_board(board)