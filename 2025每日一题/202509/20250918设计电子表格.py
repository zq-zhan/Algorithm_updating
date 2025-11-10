class Spreadsheet:

	def __init__(self, rows: int):
		self.matrix = [[0] * 26 for _ in range(rows)] 

	def setCell(self, cell: str, value: int) -> None:
		col = ord(cell[0]) - ord('A')
		row = int(cell[1:]) - 1
		self.matrix[row][col] = value

	def resetCell(self, cell: str) -> None:
		self.setCell(cell, 0)

	def getValue(self, formula: str) -> int:
		formula = formula[1:].split('+')
		X = formula[0]
		Y = formula[-1]
		if X[0].isalpha():
			col1 = ord(X[0]) - ord('A')
			row1 = int(X[1:]) - 1
			new_x = self.matrix[row1][col1]
		else:
			new_x = int(X)
		if Y[0].isalpha():
			col2 = ord(Y[0]) - ord('A')
			row2 = int(Y[1:]) - 1
			new_y = self.matrix[row2][col2]
		else:
			new_y = int(Y)
		return new_x + new_y		
        

if __name__ == '__main__':
	# s = Spreadsheet(3)
	# print(s.getValue('=5+7'))
	# s.setCell('A1', 10)
	# print(s.getValue('=A1+6'))
	# s.setCell('B2', 15)
	# print(s.getValue('=A1+B2'))
	# s.resetCell('A1')
	# print(s.getValue('=A1+B2'))
	s = Spreadsheet(657)
	s.setCell('U558', 17217)
	print(s.getValue('=59437+H286'))
	s.setCell('C164', 67231)
	s.setCell('Y294',75466)
	print(s.getValue('=Y169+Y294'))
	s.resetCell('F154')

	