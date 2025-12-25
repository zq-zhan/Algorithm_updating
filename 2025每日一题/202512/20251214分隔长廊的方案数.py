class Solution:
	def numberOfWays(self, corridor):
		MOD = 10 ** 9 + 7
		n = len(corridor)
		i = n - 1
		while i >= 0:
			if corridor[i] == 'P':
				i -= 1
				continue
			else:
				break
		corridor = corridor[:i + 1] + 'S'
		m = len(corridor)

		ans = 1
		i = cnt_s = 0
		while i < m:
			if i == m - 1 and cnt_s < 2:
				return 0
			cnt_s += int(corridor[i] == 'S')
			if cnt_s < 2:
				i += 1
				continue
			else:
				pre = i
				i += 1
				while corridor[i] == 'P':
					i += 1
				ans = ans * (i - pre) % MOD
				cnt_s = 1
				i += 1
		return ans

if __name__ == '__main__':
	corridor = "SSPPSPS"
	print(Solution().numberOfWays(corridor))