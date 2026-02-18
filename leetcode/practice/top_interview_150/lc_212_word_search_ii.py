"""
LeetCode 212 - Word Search II
https://leetcode.com/problems/word-search-ii/

"""
from typing import List

class TrieNode:
	def __init__(self):
		self.children = {}
		self.word = ''
  
def build_tree(words: List[str]) -> TrieNode:
    root = TrieNode()
    for w in words:
        node = root
        for c in w:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = w
    return root

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		trie = build_tree(words)
		dirs = [(1,0), (-1,0), (0,1), (0,-1)]
		M, N = len(board), len(board[0])
		ans = []
		def dfs(x: int, y: int, parent: TrieNode):
			tmp = board[x][y]
			node = parent.children[tmp]
			if node.word != '':
				ans.append(node.word)
				node.word = ''
			
			board[x][y] = '#'
			for dx, dy in dirs:
				nx, ny = dx + x, dy + y
				if not (0 <= nx < M and 0 <= ny < N):
					continue
				if board[nx][ny] != '#' and board[nx][ny] in node.children:
					dfs(nx, ny, node)
			board[x][y] = tmp
			if not node.children and node.word == '':
				del parent.children[tmp]

		for i in range(M):
			for j in range(N):
				if board[i][j] not in trie.children:
					continue
				dfs(i, j, trie)
		return ans					

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" ".join(row))
    print()

sol = Solution()

board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain","hklf", "hf"]
print_board(board1)
print(sol.findWords(board1, words1))
