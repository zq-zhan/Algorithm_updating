# 1.和为目标值的最长子序列长度
from functools import cache
from math import inf

class Solution1:
    def lengthOfLongestSubsequence(self, nums, target):
        n = len(nums)
        def dfs(i, c):
            # 记录每次调用的参数
            # print(f"dfs called with i={i}, c={c}")
            if i < 0:
                return 0 if c == 0 else float('-inf')
            if nums[i] > c:
                return dfs(i - 1, c)
            return max(dfs(i - 1, c), dfs(i - 1, c - nums[i]) + 1)
        
        ans = dfs(n - 1, target)
        return ans if ans > -1 else -1

# ## 递推写法
# class Solution2:
# 	def lengthOfLongestSubsequence(self, nums, target):
# 		n = len(nums)
# 		f = [[0] * (target + 1) for _ in range(n + 1)]
# 		f[0][0] = 1
# 		for i, c in enumerate(nums):
# 			for j in range(target + 1):
# 				if i < 0:
# 					f[i + 1][j] = 0 if j == 0 else -inf
# 				elif j > c:
# 					f[i + 1][j] = 0
# 				else:
# 					f[i + 1][j] = max(f[i][j], f[i][j - c] + 1)
# 		return f[n][0] if f[n][0] > -1 else -1
	
## 递推写法
class Solution2:
	def lengthOfLongestSubsequence(self, nums, target):
		n = len(nums)
		f = [[-inf] * (target + 1) for _ in range(n + 1)]
		f[0][0] = 0
		for i, c in enumerate(nums):
			for j in range(target + 1):
				if c > j:
					f[i + 1][j] = f[i][j]
				else:
					f[i + 1][j] = max(f[i][j], f[i][j - c] + 1)
		ans = f[n][target]
		return ans if ans > -1 else -1

class Solution3:
	def lengthOfLongestSubsequence(self, nums, target):
		@cache
		def dfs(i, c):
			if i < 0:
				return 0 if c == 0 else -inf
			return max(dfs(i - 1, c - nums[i]) + 1, dfs(i - 1, c))
		ans = dfs(len(nums) - 1, target)
		return ans if ans > -inf else -1

## 
class Solution4:
	def lengthOfLongestSubsequence(self, nums, target):
		n = len(nums)
		f = [[-inf] * (target + 1) for _ in range(n + 1)]
		f[0][0] = 0
		for i, x in enumerate(nums):
			for c in range(target + 1):
				if c < x:
					f[i + 1][c] = f[i][c]
				else:
					f[i + 1][c] = max(f[i][c - x] + 1, f[i][c])
		ans = f[-1][-1]
		return ans if ans > -1 else -1
	
if __name__ == '__main__':
	nums = [1,2,3,4,5]
	target = 9
	print(Solution4().lengthOfLongestSubsequence(nums, target)) # Output: 3
