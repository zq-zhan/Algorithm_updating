class Solution1:
	def lexicalOrder(self, n):
		ans = []
		v = 1
		for _ in range(n):
			ans.append(v)
			if v * 10 <= n:
				v *= 10
			else:
				while v % 10 == 9 or v + 1 > n:
					v //= 10
				v += 1
		return ans
## 递归
class Solution:
	def lexicalOrder(self, n):
		ans = []

		def dfs(cur, limit):
			if cur > limit:
				return
			ans.append(cur)
			for i in range(10):
				dfs(cur * 10 + i, limit)

		for i in range(1, 10):
			dfs(i, n)
		return ans

if __name__ == '__main__':
	n = 13
	print(Solution1().lexicalOrder(n))