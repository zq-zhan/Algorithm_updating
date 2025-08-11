class Solution:
	def numsSameConsecDiff(self, n, k):
		ans = []
		def dfs(i, x):
			if i == n:
				ans.append(x)
				return
			last = int(str(x)[-1])
			if k != 0:
				if last - k >= 0:
					dfs(i + 1, x * 10 + last - k)
				if last + k <= 9:
					dfs(i + 1, x * 10 + last + k)
				if last - k < 0 or last + k > 9:
					return
			else:
				dfs(i + 1, x * 10 + last)
		for x in range(1, 10):
			dfs(1, x)
		return ans
	
## 简化
class Solution:
	def numsSameConsecDiff(self, n, k):
		ans = []

		def dfs(i, num):
			if i == n:
				ans.append(num)
				return
			last = num % 10
			next_digits = set([last + k, last - k])
			for nxt in next_digits:
				if 0 <= nxt <= 9:
					dfs(i + 1, num * 10 + nxt)
		for x in range(1, 10):
			dfs(1, x)
		return ans
	
if __name__ == '__main__':
	n = 3
	k = 7
	print(Solution().numsSameConsecDiff(n, k))