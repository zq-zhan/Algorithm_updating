class Solution1:
	def differenceOfSums(self, n, m):
		ans = 0
		left, right = 1, n
		while left < right:
			if left % m != 0:
				ans += left
			else:
				ans -= left

			if right % m != 0:
				ans += right
			else:
				ans -= right
			left += 1
			right -= 1
		if left == right:
			ans += left if left % m != 0 else -left
		return ans


if __name__ == '__main__':
	n = 10
	m = 3
	s = Solution1()
	print(s.differenceOfSums(n, m))