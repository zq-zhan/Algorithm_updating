class Solution1:
	def maximumCandies(self, candies, k):
		left, right = 0, max(candies) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(x // mid for x in candies) >= k:
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	cnadies = [1,2,3,4,10]
	k = 5
	print(Solution1().maximumCandies(cnadies, k))