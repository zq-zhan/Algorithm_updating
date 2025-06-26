from collections import defaultdict

class Solution:
	def minGroups(self, intervals):
		dic_win = defaultdict(int)
		for left, right in intervals:
			dic_win[left] += 1
			dic_win[right + 1] -= 1
		ans = temp_s = 0
		for key, val in sorted(dic_win.items()):
			temp_s += val
			ans = max(ans, temp_s)
		return ans
	

if __name__ == '__main__':
	intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
	print(Solution().minGroups(intervals))