from functools import cache

class Solution:
	def maximumsSplicedArray(self, nums1, nums2):
		def mx_trans(arr1, arr2):
			n = len(arr1)
			diff = []
			for x, y in zip(arr1, arr2):
				diff.append(y - x)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), 0) + diff[i]
			return max(dfs(i) for i in range(n)) + sum(arr1)
		return max(mx_trans(nums1, nums2), mx_trans(nums2, nums1))

		


if __name__ == '__main__':
	nums1 = [60,60,60]
	nums2 = [10,90,10]
	print(Solution().maximumsSplicedArray(nums1, nums2))