from collections import defaultdict, Counter

class Solution1:
	def takeCharacters(self, s, k):
		dic_win = defaultdict(int)
		all_dic = Counter(s)
		if all_dic['a'] < k or all_dic['b'] < k or all_dic['c'] < k:
			return -1

		n = len(s)
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > all_dic[c] - k:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return n - ans
	
if __name__ == '__main__':
	# s = "aabaaaacaabc"
	s = "a"
	k = 1
	print(Solution1().takeCharacters(s, k))