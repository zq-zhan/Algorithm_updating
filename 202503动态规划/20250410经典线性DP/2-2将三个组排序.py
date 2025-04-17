from functools import cache

# 2.将三个组排序
class Solution1:
	def minimumOperations(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if nums[j] <= nums[i]:  # 条件成立时
					ans = max(ans, dfs(j))
			return ans + 1
		return n - max(dfs(i) for i in range(n)) 
        
if __name__ == '__main__':
	# nums = [2,1,3,2,1]
	nums = [1,3,2,1,3,3]
	print(Solution1().minimumOperations(nums)) # Output: 3