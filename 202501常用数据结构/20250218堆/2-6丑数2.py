# 13.丑数2
## 参考题解
class Solution1:
	def nthUglyNumber(self, n):
		res, a, b, c = [1] * n, 0, 0, 0
		for i in range(1, n):
			n2, n3, n5 = res[a] * 2, res[b] * 3, res[c] * 5
			res[i] = min(n2, n3, n5)
			if res[i] == n2: a += 1
			if res[i] == n3: b += 1
			if res[i] == n5: c += 1
		return res[-1]
	
if __name__ == '__main__':
	n = 10
	s = Solution1()
	print(s.nthUglyNumber(n))