from collections import defaultdict

class Solution1:
	def continuousSubarrays(self, nums):
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while max(dic_win.keys()) - min(dic_win.keys()) > 2:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	nums = [5,4,2,4]
	print(Solution1().continuousSubarrays(nums))