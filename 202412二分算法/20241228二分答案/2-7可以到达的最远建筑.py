# 8.可以到达的最远建筑
class Solution1:
	def furthestBuilding(self, heights, bricks, ladders):
		def walk(mid):
			diff_lis = []
			for i in range(1, mid + 1):
				diff_lis.append(heights[i] - heights[i - 1])

			pos_lis = []
			for x in diff_lis:
				if x > 0:
					pos_lis.append(x)
			pos_lis.sort()
			if ladders > 0 and sum(pos_lis) - sum(pos_lis[-ladders:]) <= bricks:
				return True
			elif ladders == 0 and sum(pos_lis) <= bricks:
				return True
			else:
				return False

		left, right = 0, len(heights)
		while left + 1 < right:
			mid = (left + right) // 2
			if walk(mid):
				left = mid
			else:
				right = mid
		return left

	
if __name__ == '__main__':
	heights = [4,2,7,6,9,14,12]
	bricks = 5
	ladders = 1
	print(Solution1().furthestBuilding(heights, bricks, ladders))