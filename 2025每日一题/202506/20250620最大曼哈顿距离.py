from collections import Counter, defaultdict


class Solution:
	def maxDistance(self, s, k):
		s = list(s)
		s_dic = Counter(s)
		if s_dic['N'] >= s_dic['S']:
			flag_1 = True
		if s_dic['W'] >= s_dic['W']:
			flag_2 = True

		result = ans = 0
		for i, x in enumerate(s):
			if x == 'N':
				if flag_1:
					ans += 1
				else:
					if k > 0:
						s[i] = 'S'
						k -= 1
						ans += 1
					else:
						ans -= 1
			elif x == 'S':
				if flag_1:
					if k > 0:
						s[i] = 'N'
						k -= 1
						ans += 1
					else:
						ans -= 1
				else:
					ans += 1
			elif x == 'W':
				if flag_2:
					ans += 1
				else:
					if k > 0:
						s[i] = 'E'
						k -= 1
						ans += 1
					else:
						ans -= 1
			elif x == 'E':
				if flag_2:
					if k > 0:
						s[i] = 'W'
						k -= 1
						ans += 1
					else:
						ans -= 1
				else:
					ans += 1
			result = max(result, ans)				
		return result


class Solution:
	def maxDistance(self, s, k):
		ans = 0
		cnt = defaultdict(int)
		for ch in s:
			cnt[ch] += 1
			left = k
			def f(a, b):
				nonlocal left
				d = min(a, b, left)
				left -= d
				return abs(a - b) + 2 * d
			ans = max(ans, f(cnt['N'], cnt['S']) + f(cnt['E'], cnt['W']))
		return ans

if __name__ == '__main__':
	s = 'NWSE'
	k = 1
	print(Solution().maxDistance(s, k))