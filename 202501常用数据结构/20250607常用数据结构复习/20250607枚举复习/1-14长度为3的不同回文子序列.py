from collections import Counter

class Solution:
	def countPalindromicSubsequence(self, s):
		ans = set()
		dic_k = Counter(s[1:])
		pre = s[0]
		for j in range(1, len(s) - 1):
			if dic_k[s[j]] == 1:
				del dic_k[s[j]]
			else:
				dic_k[s[j]] -= 1
			for pre in s[:j]:
				if pre in dic_k:
					ans.add((pre, s[j], pre))
		return len(ans)

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
			for j, a, b in zip(range(26), pre, suf):  # 枚举前缀和后缀的组合，将O(n)优化到常数级O(26)
				if a*b != 0:
					ans.add(chr(j + 97) + s[i] + chr(j + 97))
			pre[ord(s[i]) - ord('a')] += 1  # 维护前缀和
		return len(ans)

if __name__ == '__main__':
	s = "ckafnafqo"
	print(Solution().countPalindromicSubsequence(s))