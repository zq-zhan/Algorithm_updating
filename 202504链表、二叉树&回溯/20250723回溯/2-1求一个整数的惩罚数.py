## 灵神题解
pre_sum = [0] * 1001
for i in range(1, 1001):
	s = str(i * i)
	n = len(s)
	def dfs(p, sum):
		if p == n:
			return sum == i
		x = 0
		for j in range(p, n):  # 枚举分割出从s[p]到s[j]的子串
			x = x * 10 + int(s[j])
			if dfs(j + 1, sum + x):
				return True
		return False
	pre_sum[i] = pre_sum[i - 1] + (i * i if dfs(0, 0) else 0)
class Solution:
	def punishmentNumber(self, n):
		return pre_sum[n]
	
if __name__ == '__main__':
	n = 10
	print(Solution().punishmentNumber(n))