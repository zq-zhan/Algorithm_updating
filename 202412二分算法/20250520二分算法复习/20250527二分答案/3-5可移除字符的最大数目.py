class Solution1:
	def maximumRemovals(self, s, p, removable):
		# def check(target):
		# 	new_lis = sorted(removable[:target])
		# 	p1 = p2 = 0
		# 	for i, x in enumerate(s):
		# 		if p2 < target and i == new_lis[p2]:
		# 			p2 += 1
		# 			continue
		# 		elif x == p[p1]:
		# 				p1 += 1
		# 				if p1 == m:
		# 					return True
		# 	return False
		def check(target):
			new_lis = set(removable[:target])
			p1 = 0
			for i, x in enumerate(s):
				if i not in new_lis and x == p[p1]:
					p1 += 1
					if p1 == m:
						return True
			return False

		n, m = len(s), len(p)
		left, right = 0, len(removable) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left


if __name__ == '__main__':
	s = "abcacb"
	p = "ab"
	removable = [3,1,0]
	print(Solution1().maximumRemovals(s, p, removable))