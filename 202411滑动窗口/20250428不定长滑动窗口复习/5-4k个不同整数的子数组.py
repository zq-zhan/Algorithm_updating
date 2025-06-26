from collections import defaultdict

class Solution1:
	def subarraysWithKDistinct(self, nums, k):
		def upper_target(target):
			dic_win = defaultdict(int)
			ans = left = 0
			for c in nums:
				dic_win[c] += 1
				while len(dic_win) >= target:
					if dic_win[nums[left]] == 1:
						del dic_win[nums[left]]
					else:
						dic_win[nums[left]] -= 1
					left += 1
				ans += left
			return ans
		return upper_target(k) - upper_target(k + 1)
	
if __name__ == '__main__':
	nums = [1,2,1,2,3]
	k = 2
	print(Solution1().subarraysWithKDistinct(nums, k))