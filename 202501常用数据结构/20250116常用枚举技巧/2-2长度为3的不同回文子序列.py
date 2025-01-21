# 2.长度为3的不同回文子序列
# class Solution1:
# 	def countPalindromicSubsequence(self, s):
# 		ans = 0
# 		n = len(s)
# 		left_lis = [s[0]]
# 		right_lis = [s[-1]]
# 		for m in range(1, n - 1):
# 			left_lis.append([left_lis[m-1] + [s[m]]])
# 		for n in range(n - 2, 1, -1):
# 			right_lis.append([right_lis[n+1] + [s[n]]])

# 		for j in range(1, n - 1):
## 
class Solution2:
	def countPalindromicSubsequence(self, s):
		n = len(s)
		suf = [0] * 26
		for i in range(n - 1, -1, -1):
			suf[ord(s[i]) - ord('a')] += 1
		ans = set()
		pre = [0] * 26
		for i in range(n):
			suf[ord(s[i]) - ord('a')] -= 1  # 维护后缀和
			for j, a, b in zip(range(26), pre, suf):
				if a*b != 0:
					ans.add(chr(j + 97) + s[i] + chr(j + 97))
			pre[ord(s[i]) - ord('a')] += 1  # 维护前缀和
		return len(ans)



if __name__ == '__main__':
	s = 'aabca'
	cls = Solution2()
	print(cls.countPalindromicSubsequence(s))