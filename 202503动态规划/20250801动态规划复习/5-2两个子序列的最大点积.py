class Solution:
	def maxDotProduct(self, nums1, nums2):
		if all(x < 0 for x in nums1) and all(x > 0 for x in nums2):
			return max(nums1) * min(nums2)
		elif all(x > 0 for x in nums1) and all(x < 0 for x in nums2):
			return min(nums1) * max(nums2)

		n, m = len(nums1), len(nums2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			return max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1) + nums1[i] * nums2[j])
		return dfs(n - 1, m - 1)
	
if __name__ == '__main__':
	nums1 = [1, 1]
	nums2 = [-1, -1]
	print(Solution().maxDotProduct(nums1, nums2))