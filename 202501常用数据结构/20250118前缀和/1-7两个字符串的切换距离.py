# 7.两个字符串的切换距离
class Solution1:
	def shiftDistance(self, s, t, nextCost, previousCost):
		pre_nextCost_sum = [0]
		pre_previousCost_sum = [0]
		for p1 in range(26):
			pre_nextCost_sum.append(pre_nextCost_sum[-1] + nextCost[p1])
			pre_previousCost_sum.append(pre_previousCost_sum[-1] + previousCost[p1])

		ans = 0
		for i in range(len(s)):
			# forward = sum(pre_nextCost_sum) - (pre_nextCost_sum[ord(t[i]) - ord('a')] - pre_nextCost_sum[ord(s[i]) - ord('a')])
			back = pre_nextCost_sum[ord(t[i]) - ord('a')] - pre_nextCost_sum[ord(s[i]) - ord('a')]
			if sum(pre_previousCost_sum) >= 2 * back:
				ans += back
			else:
				ans += sum(pre_nextCost_sum) - back
		return ans

## 灵神题解
class Solution2:
	def shiftDistance(self, s, t, nextCost, previousCost):
		sigma = 26
		nxt_sum = [0] * (sigma * 2 + 1)
		pre_sum = [0] * (sigma * 2 + 1)
		for i in range(sigma * 2):
			nxt_sum[i + 1] = nxt_sum[i] + nextCost[i % sigma]
			pre_sum[i + 1] = pre_sum[i] + previousCost[i % sigma]

		ans = 0
		ord_a = ord('a')
		for x, y in zip(s, t):
			x = ord(x) - ord_a
			y = ord(y) - ord_a
			ans += min(
				nxt_sum[y + sigma if y < x else y] - nxt_sum[x],
				pre_sum[(x + sigma if x < y else x) + 1] - pre_sum[y + 1]
				)
		return ans

if __name__ == '__main__':
	s = 'abab'
	t = 'baba'
	nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	cls = Solution2()
	print(cls.shiftDistance(s, t, nextCost, previousCost))