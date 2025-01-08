# 5.可移除字符的最大数目
class Solution1:
	def maximumRemovals(self, s, p, removable):
		left, right = 0, len(removable) + 1
		n, m = len(s), len(p)
		while left + 1 < right:
			mid = (left + right) // 2
			new_removeable = removable[:mid]
			new_removeable.sort()
			p1 = p2 = p3 = 0
			while p1 < n and p3 < m:
				if p2 < mid and p1 == new_removeable[p2]:
					p1 += 1
					p2 += 1
				else:
					if s[p1] == p[p3]:
						p3 += 1
					p1 += 1 
			if p3 == m:
				left = mid
			else:
				right = mid
		return left
	
## 优化
class Solution2:
	def check(self, s, p, removable, mid):
		set_ = set(removable[:mid])
		i = 0
		for j, c in enumerate(s):
			if j not in set_ and c == p[i]:
				i += 1
				if i == len(p):
					return True
		return False

	def maximumRemovals(self, s, p, removable):
		left, right = 0, len(removable) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(s, p, removable, mid):
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	s = "abcabc"
	p = "ab"
	removable = [3,1,0]
	cls = Solution2()
	print(cls.maximumRemovals(s, p, removable))