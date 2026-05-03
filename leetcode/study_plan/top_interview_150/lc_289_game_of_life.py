"""
LeetCode 289 - Game of Life
https://leetcode.com/problems/game-of-life/

Pattern:
Matrix Simulation with In-Place State Encoding
"""
from typing import List

class Solution:
    def convert(self, cur: int, num1: int) -> int:
        if cur == 1:
            if num1 < 2:
                return 0
            if num1 == 2 or num1 == 3:
                return 1
            if num1 > 3:
                return 0
        if num1 == 3:
            return 1
    
    def encode(self, cur: int, nex: int) -> int:
        if cur == 0 and nex == 1:
            return -1
        if cur == 1 and nex == 0:
            return 2
        return cur
    
    def decode(self, encoded: int) -> tuple[int, int]:
        result = {
			0: (0, 0),
			1: (1, 1),
			-1: (0, 1),
			2: (1, 0)
		}
        return result[encoded]
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                cur = board[x][y]
                num1 = 0
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and ny >= 0 and nx < m and ny < n:
                        bef, _ = self.decode(board[nx][ny])
                        num1 += (bef == 1)
                after = self.convert(cur, num1)
                board[x][y] = self.encode(cur, after)
        for x in range(m):
            for y in range(n):
                _, board[x][y] = self.decode(board[x][y])
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol = Solution()
sol.gameOfLife(board)
print(board)