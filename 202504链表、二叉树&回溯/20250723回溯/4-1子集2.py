class Solution:
	def subsetsWithDup(self, nums):
		nums.sort()
		n = len(nums)
		ans = []
		path = []
		def dfs(i):
			if i == n:
				ans.append(path.copy())
				return
			## 选
			x = nums[i]
			path.append(x)
			dfs(i + 1)
			path.pop()

			## 不选
			i += 1
			while i < n and nums[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans
	
if __name__ == '__main__':
	nums = [1,2,2]
	print(Solution().subsetsWithDup(nums))