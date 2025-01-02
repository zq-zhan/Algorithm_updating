# 2.每个小孩最多能分到多少糖果
class Solution1:
	def maximumCandies(self, candies, k):
		left, right = 0, max(candies) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x // mid) for x in candies) >= k:
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	candies = [1,2,3,4,10]
	k = 5
	cls = Solution1()
	print(cls.maximumCandies(candies, k))