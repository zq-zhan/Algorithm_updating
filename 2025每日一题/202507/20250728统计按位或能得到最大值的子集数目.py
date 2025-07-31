# 100.统计按位或能得到最大值的子集数目
class Solution:  # O(n2^n)
	def countMaxOrSubsets(self, nums):
		ans = 0
		path = []
		ans_lis = []
		n = len(nums)
		def dfs(i, temp_s):
			nonlocal ans
			if i == n:
				ans = max(ans, temp_s)
				ans_lis.append(path.copy())
				return
			dfs(i + 1, temp_s)  # 不选
			path.append(nums[i])
			dfs(i + 1, temp_s | nums[i])  # 选
			path.pop()
		dfs(0, 0)
		result = 0
		for path in ans_lis:
			pre = 0
			for x in path:
				pre |= x
			result += int(pre == ans)
		return result

	
if __name__ == '__main__':
	nums = [3,1]
	print(Solution().countMaxOrSubsets(nums))