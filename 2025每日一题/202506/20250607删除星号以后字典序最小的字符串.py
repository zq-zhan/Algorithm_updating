class Solution1:
	def clearStars(self, s):
		s = list(s)
		st = [[] for _ in range(26)]
		for i, x in enumerate(s):
			if x != '*':
				st[ord(x) - ord('a')].append(i)
			else:
				for val in st:
					if val:
						s[val.pop()] = '*'
						break
		return ''.join(x for x in s if x != '*')
	
if __name__ == '__main__':
	s = "aaba*"
	print(Solution1().clearStars(s))