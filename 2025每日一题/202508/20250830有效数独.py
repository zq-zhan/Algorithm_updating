class Solution:
	def isValidSudoku(self, board):
		for row in board:
			a = [x for x in row if x != '.']
			if len(a) != len(set(a)):
				return False
		for j in range(9):
			b = [row[j] for row in board if row[j] != '.']
			if len(b) != len(set(b)):
				return False
		target = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]
		for x, y in target:
			a = set()
			for diff1 in (-1, 0, 1):
				for diff2 in (-1, 0, 1):
					num = board[x + diff1][y + diff2]
					if num != '.':
						if num not in a:
							a.add(num)
						else:
							return False
		return True

if __name__ == '__main__':
	board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
	print(Solution().isValidSudoku(board))