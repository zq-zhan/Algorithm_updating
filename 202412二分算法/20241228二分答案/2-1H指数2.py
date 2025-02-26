# 1.H指数2
class Solution1:
	def check(self, citations, mid):
		for i,c in enumerate(citations):
			if c >= mid:
				break
		return (len(citations) - i) >= mid
	def hIndex(self, citations):
		left, right = -1, citations[-1] + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(citations, mid):
				left = mid
			else:
				right = mid
		return left
	
class Solution:
	def check(self, citations, mid):
		for i,c in enumerate(citations):
			if c >= mid:
				break
		return (len(citations) - i) >= mid
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(citations, mid):
				left = mid
			else:
				right = mid
		return left

## 灵神思路优化
class Solution2:
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if citations[-mid] >= mid:
				left = mid
			else:
				right = mid
		return left


class Solution3:
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(x // mid >= 1 for x in citations) >= mid:
				left = mid
			else:
				right = mid
		return left

	
if __name__ == '__main__':
	citations = [100]
	cls = Solution3()
	print(cls.hIndex(citations))