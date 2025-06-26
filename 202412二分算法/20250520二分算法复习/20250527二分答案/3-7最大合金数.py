class Solution1:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		def check(target):
			for target_composition in composition:
				ans = 0
				for i, x in enumerate(target_composition):
					ans += max((target * x - stock[i]), 0) * cost[i]
				if ans <= budget:
					return True
			return False

		# composition.sort(key = lambda x: sum(x))
		left, right = 0, budget + max(stock) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left


	
if __name__ == '__main__':
	n = 2
	k = 3
	budget = 10
	composition = [[2,1],[1,2],[1,1]]
	stock = [1,1]
	cost = [5,5]
	print(Solution1().maxNumberOfAlloys(n, k, budget, composition, stock, cost))