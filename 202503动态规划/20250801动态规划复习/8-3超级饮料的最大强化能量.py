from functools import cache

class Solution:
	def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
		n = len(energyDrinkA)
		@cache
		def dfs(i, state):
			if i < 0:
				return 0
			if state == 0:
				return max(dfs(i - 1, 0), dfs(i - 2, 1)) + energyDrinkA[i]
			return max(dfs(i - 1, 1), dfs(i - 2, 0)) + energyDrinkB[i]
		return max(dfs(n - 1, 0), dfs(n - 1, 1))
	
if __name__ == '__main__':
	energyDrinkA = [1, 3, 1]
	energyDrinkB = [3, 1, 1]
	print(Solution().maxEnergyBoost(energyDrinkA, energyDrinkB))