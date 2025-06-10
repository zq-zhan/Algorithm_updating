from collections import defaultdict
from math import inf

class Solution:
	def maxDistance(self, arrays):
		ans = 0
		mn = inf
		mx = -inf
		# dic_win = defaultdict(int)
		for new_arr in arrays:
			ans = max(ans, new_arr[-1] - mn, mx - new_arr[0])
			mn = min(mn, new_arr[0])
			mx = max(mx, new_arr[-1])
		return ans

if __name__ == '__main__':
	arrays = [[-3,-3],[-3,-2]]
	s = Solution()
	print(s.maxDistance(arrays))