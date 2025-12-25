class Solution:
	def numberOfSubstrings(self, s):
		n = len(s)
		ans = 0
		for length in range(1, n + 1):
			for i in range(0, n - length + 1):
				cnt_1 = s[i:i + length].count('1')
				cnt_0 = length - cnt_1
				if cnt_1 >= cnt_0 ** 2:
					ans += 1
		return ans

if __name__ == '__main__':
	s = "101101"
	print(Solution().numberOfSubstrings(s))