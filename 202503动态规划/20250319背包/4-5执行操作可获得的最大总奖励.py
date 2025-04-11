from functools import cache

class Solution1:
	def maxTotalReward(self, rewardValues):
		rewardValues.sort(reverse=True)
		ans = 0
		@cache
		def dfs(i, c):
			nonlocal ans
			if i < 0:
				ans = max(ans, c)
				return ans
			if rewardValues[i] > c:
				return max(dfs(i - 1, c + rewardValues[i]), dfs(i - 1, c))
			else:
				return dfs(i - 1, c)
		return dfs(len(rewardValues) - 1, 0)
	
## 灵神思路
class Solution2:
	def maxTotalReward(self, rewardValues):
		nums = sorted(set(rewardValues))
		m = nums[-1]  # 最大值
		f = [False] * 2 * m
		f[0] = True
		for v in nums:
			for c in range(2 * m):
				if v <= c < 2 * v:
					f[c] = f[c] | f[c - v]
		ans = 2 * m - 1
		while not f[ans]:
			ans -= 1
		return ans
	
## 递归写法
class Solution3:
	def maxTotalReward(self, rewardValues):
		nums = sorted(set(rewardValues))
		m = nums[-1]
		@cache
		def dfs(i, c):
			if i < 0:
				return True if c == 0 else False
			if nums[i] <= c < 2 * nums[i]:
				return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
			else:
				return dfs(i - 1, c)
		ans = 2 * m - 1
		n = len(nums)
		while not dfs(n - 1, ans):
			ans -= 1
		return ans

class Solution4:
	def maxTotalReward(self, rewardValues):
		nums = sorted(set(rewardValues), reverse = True)
		@cache
		def dfs(i, c):
			if i < 0:
				return c
			if nums[i] <= c:
				return dfs(i - 1, c)
			return max(dfs(i - 1, c), dfs(i - 1, c + nums[i]))
		return dfs(len(nums) - 1, 0)

if __name__ == '__main__':
	rewardValues = [1,1,3,3]
	print(Solution4().maxTotalReward(rewardValues))