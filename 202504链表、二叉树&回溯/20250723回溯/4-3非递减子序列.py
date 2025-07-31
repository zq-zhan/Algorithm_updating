class Solution:
	def findSubsequences(self, nums):
		ans = []
		path = []
		n = len(nums)
		def dfs(i):
			if i == n:
				if len(path) >= 2:
					ans.append(path.copy())
				return

			## 选
			x = nums[i]
			if not path or x >= path[-1]:
				path.append(x)
				dfs(i + 1)
				path.pop()

			## 不选——这种解法必须要排序
			i += 1
			while i < n and nums[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans

class Solution:  
	def findSubsequences(self, nums):
		ans = []
		n = len(nums)

		def dfs(i, path):
			if len(path) >= 2:
				if path[-1] >= path[-2]:
					ans.append(path)
				else:
					return

			for j in range(i, n):
				if nums[j] in nums[i:j]:  # 去重，不选
					continue
				dfs(j + 1, path + [nums[j]])  # 选
		dfs(0, [])
		return ans


	
if __name__ == '__main__':
	nums = [1,2,2]
	print(Solution().findSubsequences(nums))