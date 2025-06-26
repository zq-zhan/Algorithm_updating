class Solution1:
	def getLongestSubsequence(self, words, groups):
		ans = []
		for i, c in enumerate(groups):
			if i == 0 or groups[i] != groups[i - 1]:
				ans.append(words[i])
		return ans
	
if __name__ == '__main__':
	words = ['a', 'b', 'c', 'd']
	groups = [1,0,1,1]
	print(Solution1().getLongestSubsequence(words, groups))