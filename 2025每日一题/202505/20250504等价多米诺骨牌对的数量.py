class Solution1:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		n = len(dominoes)
		for i in range(n):
			for j in range(i + 1, n):
				if dominoes[i] == dominoes[j] or dominoes[i][::-1] == dominoes[j]:
					ans += 1
		return ans
## 灵神题解
class Solution2:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		cnt = defaultdict(int)
		for d in dominoes:
			d = tuple(sorted(d))
			ans += cnt[d]
			cnt[d] += 1
		return ans