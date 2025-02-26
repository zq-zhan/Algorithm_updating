# 9.重构字符串
from collections import Counter

class Solution1:
	def reorganizeString(self, s):
		s_dic = Counter(s)
		n = len(s)
		ch, m = s_dic.most_common(1)[0]  # 获取最常出现的字符及其次数
		if m > n - m + 1:
			return ''

		ans = [''] * n
		i = m * 2
		ans[:i:2] = [ch] * m
		del s_dic[ch]

		for ch, cnt in s_dic.items():
			for _ in range(cnt):
				if i >= n:
					i = 1  
				ans[i] = ch
				i += 2
		return ''.join(ans)
	
if __name__ == '__main__':
	s = 'aaabbbcc'
	print(Solution1().reorganizeString(s))