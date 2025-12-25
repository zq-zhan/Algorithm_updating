class Solution:
	def countPermutations(self, complexity):
		MOD = 10 ** 9 + 7

		mn, mx = min(complexity), max(complexity)
		cnt_lis = [0] * (mx - mn + 1)
		cnt_lis[complexity[0] - mn] += 1
		ans = 1
		for x in complexity[1:]:
			cnt = sum(cnt_lis[:x - mn])
			ans = (ans * cnt) % MOD
			cnt_lis[x - mn] += 1
			if ans == 0:
				return 0
		return ans


if __name__ == '__main__':
	complexity = [1,2,3]
	print(Solution().countPermutations(complexity))