from collections import defaultdict

class Solution:
	def numPairsDivisibleBy60(self, time):
		dic_win = defaultdict(int)
		ans = 0
		for x in time:
			ans += dic_win[60 - x % 60]
			if x % 60 == 0:
				dic_win[60] += 1
			else:
				dic_win[x % 60] += 1
		return ans

if __name__ == '__main__':
	time = [30,20,150,100,40]
	print(Solution().numPairsDivisibleBy60(time))