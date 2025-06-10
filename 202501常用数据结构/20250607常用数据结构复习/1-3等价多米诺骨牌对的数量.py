from collections import defaultdict

class Solution:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		dic_win = defaultdict(int)
		for a, b in dominoes:
			temp = (a, b) if a <= b else (b, a)
			if temp in dic_win: 
				ans += dic_win[temp]
			dic_win[temp] += 1
		return ans
	
if __name__ == '__main__':
	dominoes = [[1,2],[2,1],[3,4],[5,6]]
	print(Solution().numEquivDominoPairs(dominoes))