from collections import defaultdict

class Solution1:  # 错解，无法知道哪个等值数
	def longestEqualSubarray(self, nums, k):
		ans = left = 0
		n = len(nums)
		cnt = 0
		for right in range(1, n):
			cnt += int(nums[right] != nums[left])
			while cnt > k:
				cnt -= int(nums[right] != nums[left])
				left += 1
			ans = max(ans, right - left + 1 - cnt)
		return ans
	
class Solution2:
	def longestEqualSubarray(self, nums, k):
		dic_win = defaultdict(int)
		ans = left = cnt = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			cnt += 1 if len(dic_win) > 1 else 0
			while len(dic_win) > 1 and cnt > k:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
				cnt -= 1
			ans = max(ans, max(dic_win.values()) - cnt)
		return ans


if __name__ == '__main__':
	nums = [1,3,2,3,1,3]
	k = 3
	print(Solution2().longestEqualSubarray(nums, k))