from collections import Counter

class Solution1:
	def minWindow(self, s, t):
		if s == t:
			return s
		t_dic = Counter(t)
		ans = s + '0'
		left = 0
		for right, c in enumerate(s):
			t_dic[c] -= 1
			while max(t_dic.values()) <= 0:
				if max(t_dic.values()) == 0:
					temp_str = s[left:right + 1]
					if len(temp_str) < len(ans) or (len(temp_str) == len(ans) and temp_str < ans):
						ans = s[left:right + 1]
				t_dic[s[left]] += 1
				left += 1
		return ans if len(ans) <= len(s) else ''

if __name__ == '__main__':
	s = "ADOBECODEBANC"
	t = "ABC"
	print(Solution1().minWindow(s, t))