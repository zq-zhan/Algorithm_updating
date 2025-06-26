from collections import defaultdict

class Solution1:
	def countLargestGroup(self, n):
		dic_win = defaultdict(int)
		max_cnt = ans = 0  # max_cnt为数字数目并列最多的个数
		for x in range(1, n + 1):
			val = 0
			for char in str(x):
				val += int(char)
			dic_win[val] += 1
			if dic_win[val] > max_cnt:
				max_cnt = dic_win[val]
				ans = 1
			elif dic_win[val] == max_cnt:
				ans += 1
		# max_cnt = max(dic_win.values())
		# return sum(int(val == max_cnt) for val in dic_win.values())
		return ans

if __name__ == '__main__':
	n = 13
	print(Solution1().countLargestGroup(n))