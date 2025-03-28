# 16.提取至多k个元素的最大总和
class Solution1:
	def maxSum(self, grid, limits, k):
		temp_lis = []
		for i, value_lis in enumerate(grid):
			for x in value_lis:
				temp_lis.append([i, x])
		temp_lis = sorted(temp_lis, key = lambda lis:-lis[1])

		ans = 0
		# cnt = 0
		for i, x in temp_lis:
			if limits[i] > 0:
				ans += x if k > 0 else 0
				k -= 1
				limits[i] -= 1
				if k == 0:
					return ans
			else:
				continue
		return ans

	
if __name__ == '__main__':
	grid = [[29,13]]
	limits = [2]
	k = 0
	print(Solution1().maxSum(grid, limits, k))