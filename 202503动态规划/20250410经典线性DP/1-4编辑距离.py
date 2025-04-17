from functools import cache

# 4.编辑距离
class Solution1:
	def minDistance(self, word1, word2):
		n = len(word1)
		m = len(word2)
		# while n < m:
		# 	word1 += str('0')
		# 	n += 1
		@cache
		def dfs(i, j):
			if i < 0:
				return j + 1
			if j < 0:
				return i + 1
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + 1, dfs(i - 1, j - 1) + 1, dfs(i, j - 1) + 1)  #分别为删除、替换、插入
		return dfs(n - 1, m - 1)
	
if __name__ == '__main__':
	word1 = "horse"
	word2 = "ros"
	print(Solution1().minDistance(word1, word2))