## 超时
class Solution:
	def maxOperations(self, s):
		s = list(map(int, s))
		cnt_1 = s.count(1)
		ans = 0
		n = len(s)
		while sum(s[-cnt_1:]) != cnt_1:
			tag = False
			for i in range(n - 1):
				if s[i] - s[i + 1] == 1:
					s[i + 1], s[i] = s[i], s[i + 1]
					tag = True
					ans += int(i == n - 2)
				else:
					if tag == True:
						ans += 1
						break
		return ans
## 灵神题解
class Solution:
	def maxOperations(self, s):
		ans = cnt1 = 0
		for i, c in enumerate(s):
			if c == '1':
				cnt1 += 1
			elif i > 0 and s[i - 1] == '1':
				ans += cnt1
		return ans

if __name__ == '__main__':
	s = "1001101"
	print(Solution().maxOperations(s))