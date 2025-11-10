class Solution:
	def hasSameDigits(self, s):
		s = list(map(int, s))
		while len(s) > 2:
			temp_s = ''
			n = len(s)
			for i in range(n - 1):
				temp_s += str((s[i] + s[i + 1]) % 10)
			s = list(map(int, temp_s))
		return s[0] == s[1]

## 优化
class Solution:
	def hasSameDigits(self, s):
		n = len(s) - 1
		cur = 1  # C(n - 1, 0)
		sum1, sum2 = 0, 0
		for i in range(n):
			sum1 = (sum1 + int(s[i]) * cur) % 10
			sum2 = (sum2 + int(s[i + 1]) * cur) % 10
			if i < n - 1:
				cur *= (n - 1 - i) / (i + 1)  # C(n - 1, 1) = C(n - 1, 0) * (n - 1 - 0) // (0 + 1)
		return sum1 == sum2
	
if __name__ == '__main__':
	s = "3902"
	print(Solution().hasSameDigits(s))