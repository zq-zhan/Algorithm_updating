class Solution1:
	def shipWithinDays(self, weights, days):
		def check(target):
			temp_s = cnt = 0
			for x in weights:
				if temp_s + x <= target:
					temp_s += x
					continue
				temp_s = x
				cnt += 1
			return cnt + 1 <= days

		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

	
if __name__ == '__main__':
	weights = [1,2,3,1,1]
	days = 4
	print(Solution1().shipWithinDays(weights, days))