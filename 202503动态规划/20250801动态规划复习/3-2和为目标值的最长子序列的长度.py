class Solution:
	def lengthOfLongestSubsequence(self, nums, target):
		ans = -1
		path_s = 0
		def dfs(i, path_len):
			nonlocal ans, path_s
			if i < 0:
				if path_s == target:
					ans = max(ans, path_len)
				return
			# 选
			path_s += nums[i]
			dfs(i - 1, path_len + 1)
			path_s -= nums[i]

			## 不选
			dfs(i - 1, path_len)
		dfs(len(nums) - 1, 0)
		return ans
	
if __name__ == '__main__':
	nums = [1,2,3,4,5]
	target = 9
	print(Solution().lengthOfLongestSubsequence(nums, target))