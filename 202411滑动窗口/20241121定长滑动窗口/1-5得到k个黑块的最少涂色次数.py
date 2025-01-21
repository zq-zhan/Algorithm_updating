# 5.得到k个黑块的最少涂色次数
class Solution1:
	def minimumRecolors(self, blocks, k):
		ans = len(blocks)
		temp_cnt = 0
		for i, c in enumerate(blocks):
			if c == 'W':
				temp_cnt += 1
			if i < k - 1:
				continue
			ans = min(ans, temp_cnt)
			if blocks[i - k + 1] == 'W':
				temp_cnt -= 1
		return ans

if __name__ == '__main__':
	blocks = "WBBWWBBWBW"
	k = 7
	print(Solution1().minimumRecolors(blocks, k))