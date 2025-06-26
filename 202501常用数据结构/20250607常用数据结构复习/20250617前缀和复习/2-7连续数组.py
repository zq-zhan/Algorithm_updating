from collections import defaultdict

class Solution:
	def findMaxLength(self, nums):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		ans = pre_s = 0
		for i, nums in enumerate(nums):
			pre_s += 1 if nums == 1 else -1
			pre_index = dic_win.get(pre_s, i)
			if pre_index == i:
				dic_win[pre_s] = i
			else:
				ans = max(ans, i - pre_index)  # 因为pre_index 始终是最早出现的那个index
		return ans
	
if __name__ == '__main__':
	nums = [0,1,1,1,1,1,0,0,0]
	print(Solution().findMaxLength(nums))