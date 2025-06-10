class Solution:
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			# if sum(int(x >= mid) for x in citations) >= mid:
			if citations[-mid] >= mid:
				left = mid
			else:
				right = mid
		return left

if __name__ == '__main__':
	citations = [1,2,100]
	print(Solution().hIndex(citations))