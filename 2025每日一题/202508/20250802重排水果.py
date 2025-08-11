from collections import defaultdict

## 灵神题解——贪心
class Solution:
	def minCost(self, basket1, basket2):
		cnt = defaultdict(int)
		for x, y in zip(basket1, basket2):
			cnt[x] += 1
			cnt[y] -= 1  # 交集元素互相抵消

		a, b = [], []
		for x, c in cnt.items():
			if c % 2:  # 奇数无法均分
				return -1
			if c > 0:  # 剩余元素一半放入a或b
				a.extend([x] * (c // 2))
			else:
				b.extend([x] * (-c // 2))
		a.sort()
		b.sort(reverse = True)
		mn = min(cnt)
		return sum(min(x, y, mn*2) for x, y in zip(a, b))
	
if __name__ == '__main__':
	basket1 = [84,80,43,8,80,88,43,14,100,88]
	basket2 = [32,32,42,68,68,100,42,84,14,8]
	print(Solution().minCost(basket1, basket2))