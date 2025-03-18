# 越长越合法
from collections import defaultdict

# 1.包含所有三种字符的子字符串数目
class Solution1:
	def numberOfSubstrings(self, s):
		ans = left = 0
		dic_win = {'a':0, 'b':0, 'c':0}
		for right, c in enumerate(s):
			dic_win[c] += 1
			if min(dic_win.values()) < 1:
				continue
			ans += left + 1
			dic_win[s[left]] -= 1
			left += 1
		return ans
## 灵神题解
class Solution2:
	def numberOfSubstrings(self, s):
		ans = left = 0
		dic_win = {'a':0, 'b':0, 'c':0}
		for right, x in enumerate(s):
			dic_win[x] += 1
			while min(dic_win.values()) >= 1:
				dic_win[s[left]] -= 1
				left += 1
				# left += 1
			ans += left
		return ans

## 
class Solution3:
	def numberOfSubstrings(self, s):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while len(dic_win) == 3:
				ans += left + 1
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			# ans += left
		return ans
	
if __name__ == '__main__':
	s = "aaacb"
	cls = Solution3()
	print(cls.numberOfSubstrings(s))