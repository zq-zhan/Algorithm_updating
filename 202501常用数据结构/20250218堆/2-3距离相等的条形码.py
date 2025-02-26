# 10.距离相等的条形码
from collections import Counter

class Solution1:
	def rearrangeBarcodes(self, barcodes):
		n = len(barcodes)
		bar_dict = Counter(barcodes)  # O(n)
		ch, m = bar_dict.most_common(1)[0]  # O(1)
		ans = [0] * n

		i = m * 2
		ans[:i:2] = [ch] * m
		del bar_dict[ch]
		for ch, cnt in bar_dict.items():  # O(|sigma|) 字符串去重的长度
			for _ in range(cnt):
				if i >= n:
					i = 1
				ans[i] = ch
				i += 2
		return ans
	
##
class Solution2:
	def rearrangeBarcodes(self, barcodes):
		n = len(barcodes)
		bar_dict = Counter(barcodes).most_common()  # O(n + klogk)
		if bar_dict[0][1] > (n - 1) // 2 + 1:
			return ''

		ans = [0] * n
		idx = 0
		for ch, cnt in bar_dict: # O(k)
			for _ in range(cnt):
				ans[idx] = ch
				idx += 2
				if idx >= n:
					idx = 1
		return ans


if __name__ == '__main__':
	barcodes = [1,1,1,2,2,2]
	s = Solution1()
	print(s.rearrangeBarcodes(barcodes))