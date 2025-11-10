class Solution:
	def minCost(self, colors, neededTime):
		ans = 0
		n = len(colors)
		for i in range(1, n):
			if colors[i] == colors[i - 1]:
				if neededTime[i] < neededTime[i - 1]:
					ans += neededTime[i]
					neededTime[i] = neededTime[i - 1]
				else:
					ans += neededTime[i - 1]
		return ans
	
if __name__ == '__main__':
	colors = "abaac"
	neededTime = [1,2,3,4,5]
	print(Solution().minCost(colors, neededTime))