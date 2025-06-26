class Solution1:
	def maxValue(self, n, index, maxSum):
		# def check(target):
		# 	temp = target
		# 	ans = 0
		# 	for i in range(index, -1, -1):
		# 		ans += max(temp, 1)
		# 		temp -= 1
		# 	for i in range(index + 1, n):
		# 		target -= 1
		# 		ans += max(target, 1)
		# 	return ans <= maxSum
		def check(target):
			ans = 0
			if index + 1 <= target:
				m = index + 1
				ans += m * (target + target - m + 1) // 2
			else:
				m = target
				ans += m * (1 + m) // 2 + index - target + 1

			if n - target <= target:
				m = n - index
				ans += m * (target + target - m + 1) // 2 - target
			else:
				m = target
				ans += m * (1 + m) // 2 + n - target - 1 - target
			return ans <= maxSum

		left, right = 1, maxSum - n + 2
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	n = 1
	index = 0
	maxSum = 24
	s = Solution1()
	print(s.maxValue(n, index, maxSum))