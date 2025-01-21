# 1、乘法表中第k小的数
class Solution1:  # O(n^2)超出时间限制
	def findKthNumber(self, m, n, k):
		new_arr = []
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				new_arr.append(i * j)
		new_arr.sort()

		def check(mn):
			ans = 0
			for x in new_arr:
				if x <= mn:
					ans += 1
					if ans >= k:
						return True
				else:
					return False

		left, right = new_arr[0] - 1, new_arr[-1]
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
## 灵神优化题解
class Solution2:
	def findKthNumber(self, m, n, k):
		def check(mn):
			cnt = 0
			for i in range(1, m + 1):
				cnt += min(mn // i, n)
			return cnt >= k

		left, right = 0, m * n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 2.有序矩阵中第k小的元素
class Solution1:
	def kthSmallest(self, matrix, k):
		def check(x):
			p1 = 0
			p2 = n - 1
			cnt = 0
			while p1 < n and p2 >= 0:
				if matrix[p1][p2] <= x:
					cnt += p2 + 1
					p1 += 1
				else:
					p2 -= 1
			return cnt >= k

		n = len(matrix)
		left, right = matrix[0][0] - 1, matrix[n-1][n-1]
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
