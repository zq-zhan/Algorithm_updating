from functools import cache

# class Solution:
# 	def wiggleMaxLength(self, nums):
# 		if len(nums) == 2 and sum(nums) == 0:
# 			return 1

# 		n = len(nums)
# 		@cache
# 		def dfs(i, pre1, pre2):
# 			if i == n:
# 				return 0
# 			if pre1 == -1 or pre2 == -1 or (pre1 - pre2) * (nums[i] - pre1) < 0:
# 				return max(dfs(i + 1, nums[i], pre1) + 1, dfs(i + 1, pre1, pre2))
# 			return dfs(i + 1, pre1, pre2)
# 		return dfs(0, -1, -1)
## 回溯解法
class Solution:
	def wiggleMaxLength(self, nums):
		n = len(nums)
		ans = 1
		def dfs(i, path):
			nonlocal ans
			ans = max(ans, len(path))
			if i == n:
				return
			
			## 不选
			if (len(path) > 1 and (path[-1] - path[-2]) * (nums[i] - path[-1]) >= 0) or (len(path) >= 1 and path[-1] == nums[i]):
				dfs(i + 1, path)	
			else:		
				## 选
				path.append(nums[i])
				dfs(i + 1, path)
				path.pop()  # 回溯
		dfs(0, [])
		return ans


	
if __name__ == '__main__':
	nums = [0,0]
	print(Solution().wiggleMaxLength(nums))