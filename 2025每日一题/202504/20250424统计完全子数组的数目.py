from collections import defaultdict

# 20250424统计完全子数组的数目
class Solution1:
	def countCompleteSubarrays(self, nums):
		n = len(set(nums))
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while len(dic_win) == n:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans
	
if __name__ == '__main__':
	nums = [1,3,1,2,2]
	print(Solution1().countCompleteSubarrays(nums))