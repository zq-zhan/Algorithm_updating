from itertools import accumulate

class Solution:
	def shiftDistance(self, s, t, nextCost, previousCost):
		ord_a = ord('a')
		nextCost += nextCost
		previousCost += previousCost
		for i in range(1, 52):
			nextCost[i] += nextCost[i - 1]
			previousCost[i] += previousCost[i - 1]

		nextCost = [0] + nextCost
		previousCost = [0] + previousCost

		n = len(s)
		ans = 0
		for i in range(n):
			ord_s = ord(s[i]) - ord_a
			ord_t = ord(t[i]) - ord_a
			if ord_s < ord_t:
				ans += min(nextCost[ord_t] - nextCost[ord_s], previousCost[ord_s + 26 + 1] - previousCost[ord_t])
			else:
				ans += min(nextCost[ord_s + 26] - nextCost[ord_t], previousCost[ord_s + 1] - previousCost[ord_t + 1])
		return ans
	
## 灵神题解
class Solution1:
	def shiftDistance(self, s, t, nextCost, previousCost):
		nxt_sum = list(accumulate(nextCost + nextCost, initial = 0))
		pre_sum = list(accumulate(previousCost + previousCost, initial = 0))

		ans = 0
		ord_a = ord('a')
		for x, y in zip(s, t):
			x = ord(x) - ord_a
			y = ord(y) - ord_a
			ans += min(nxt_sum[y + 26 if y < x else y] - nxt_sum[x],
						pre_sum[(x + 26 if x < y else x) + 1] - pre_sum[y + 1])
		return ans


if __name__ == '__main__':
	s = "abab"
	t = "baba"
	nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	sol = Solution()
	print(sol.shiftDistance(s, t, nextCost, previousCost))