from math import inf

class Solution:
	def maxScoreSightseeingPair(self, values):
		ans = 0
		for i, x in enumerate(values):
			for j in range(i + 1, len(values)):
				ans = max(ans, x + values[j] + i - j)
		return ans
class Solution:
	def maxScoreSightseeingPair(self, values):
		ans = 0
		mx = -inf
		for j, x in enumerate(values):
			ans = max(ans, mx + x - j)
			mx = max(mx, x + j)
		return ans
	
if __name__ == '__main__':
	values = [8,1,5,2,6]
	print(Solution().maxScoreSightseeingPair(values))