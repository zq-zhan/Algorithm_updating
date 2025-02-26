# 11.你可以工作的最大周数
from collections import defaultdict

class Solution1:
	def numberOfWeeks(self, milestones):
		n = sum(milestones)
		temp_dict = defaultdict()
		# max_char = max_cnt = 
		for i, x in enumerate(milestones):  # O(k)
			temp_dict[i] = x

		ans_lis = [0] * n
		idx = 0
		for ch, cnt in temp_dict.items():
			for _ in range(cnt):
				ans_lis[idx] = ch
				idx += 2
				if idx >= n:
					idx = 1
					break
		ans = 1
		for i in range(1, n):
			if ans_lis[i] == ans_lis[i - 1]:
				break
			ans += 1
		return ans

if __name__ == '__main__':
	milestones = [1000000]
	print(Solution1().numberOfWeeks(milestones))