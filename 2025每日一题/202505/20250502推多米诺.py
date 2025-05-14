class Solution1:
	def pushDominoes(self, deminoes):
		# ans = ''
		deminoes = '.' + deminoes + '.'
		deminoes = list(deminoes)
		n = len(deminoes)
		for i in range(1, n - 1):
			if deminoes[i] == '.':
				if deminoes[i + 1] == 'L' and deminoes[i - 1] != 'R':
					deminoes[i] = 'L'
				elif deminoes[i - 1] == 'R' and deminoes[i + 1] != 'L':
					deminoes[i] = 'R'
		return ''.join(deminoes[1:-1])


class Solution:
	def pushDominoes(self, deminoes):
		deminoes = list('L' + deminoes + 'R')
		n = len(deminoes)
		pre = 0
		ans = ''
		for i, c in enumerate(deminoes):
			if c == '.':
				continue
			elif c == deminoes[pre]:
				deminoes[pre + 1: i] = c * (i - pre - 1)
			elif c == 'L':
				m = (pre + i - 1) // 2
				deminoes[pre + 1:m + 1] = 'R' * (m - pre)
				m = (pre + i) // 2 + 1
				deminoes[m:i] = 'L' * (i - m)
			pre = i
		return ''.join(deminoes[1:-1])

if __name__ == '__main__':
	deminoes = "..R.."
	print(Solution().pushDominoes(deminoes))