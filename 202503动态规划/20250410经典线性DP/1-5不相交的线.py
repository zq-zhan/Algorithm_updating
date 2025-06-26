from functools import cache

# 5.不相交的线
class Solution1:
	def maxUncrossedLines(self, nums1, nums2):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums1[i] == nums2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(len(nums1) - 1, len(nums2) - 1)
	
if __name__ == '__main__':
	nums1 = [1, 4, 2]
	nums2 = [1, 2, 4]
	print(Solution1().maxUncrossedLines(nums1, nums2)) # Output: 2