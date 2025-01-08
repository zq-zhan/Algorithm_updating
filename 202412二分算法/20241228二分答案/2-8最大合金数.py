# 9.最大合金数
from cmath import inf


class Solution1:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		def check(mid):
			temp_min = inf
			for i in range(k):
				min_composition = - sum(a * b for a,b in zip(stock, cost))
				min_composition += sum(a * b for a,b in zip(composition[i], cost))
				temp_min = min(min_composition, temp_min)
			return temp_min <= budget

		left, right = 0, max(stock) + budget // sum(cost) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left 
	

## 灵神思路
class Solution2:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		ans = 0
		mx = min(stock) + budget
		for comp in composition:
			def check(num):
				money = 0
				for s, base, c in zip(stock, comp, cost):
					if s < base * num:
						money += (base * num - s) * c
						if money > budget:
							return False
				return True

			left, right = ans, mx + 1
			while left + 1 < right:
				mid = (left + right) // 2
				if check(mid):
					left = mid
				else:
					right = mid
			ans = left
		return ans
	
	
if __name__ == '__main__':
	n = 3
	k = 2
	budget = 15
	composition = [[1, 1, 1], [1, 1, 10]]
	stock = [0, 0, 0]
	cost = [1, 2, 3]
	s = Solution2()
	print(s.maxNumberOfAlloys(n, k, budget, composition, stock, cost))