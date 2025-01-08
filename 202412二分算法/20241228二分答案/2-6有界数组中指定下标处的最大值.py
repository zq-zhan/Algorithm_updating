# 6.有界数组中指定下标处的最大值
class Solution1:
	def check(self, n, index, maxSum, mid):
		ans = mid
		temp = mid
		for i in range(index + 1, n):
			# ans += max(temp - 1, 1)
			temp = max(temp - 1, 1)
			ans += temp
		temp = mid
		for j in range(index - 1, -1, -1):
			temp = max(temp - 1, 1)
			ans += temp
		return ans <= maxSum

	def maxValue(self, n, index, maxSum):
		left, right = 1, maxSum - n + 2
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(n, index, maxSum, mid):
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	n = 1
	index = 0
	maxSum = 24
	cls = Solution1()
	print(cls.maxValue(n, index, maxSum))