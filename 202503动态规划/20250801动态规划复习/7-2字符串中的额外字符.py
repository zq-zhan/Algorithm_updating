from functools import cache
from math import inf

class Solution:
	def minExtraChar(self, s, dictionary):
		dictionary = set(dictionary)
		mn_len = min(list(map(len, dictionary)))
		@cache
		def dfs(i):
			if i < mn_len - 1:
				return max(0, i + 1)
			res = dfs(i - 1) + 1
			for j in range(i + 1):
				if s[j:i + 1] in dictionary:
					res = min(res, dfs(j - 1))
					# break  不能加break，因为当前保留最长的不一定是结果最好的（反贪心思想）
			# res = min(res, )
			return res
		return dfs(len(s) - 1)
	

# class Solution:
# 	def minExtraChar(self, s, dictionary):
# 		dictionary = set(dictionary)
# 		wordLen = set(map(len, dictionary))
# 		@cache
# 		def dfs(i):
# 			if i < min(wordLen) - 1:
# 				return max(0, i + 1)
# 			ans = dfs(i - 1) + 1  # 不选的时候ans最大
# 			for length in wordLen:
# 				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
# 					ans = min(ans, dfs(i - length))
# 			return ans
# 		return dfs(len(s) - 1)
	
if __name__ == '__main__':
    s = "aaaa"
    dictionary = ["aa", "aaa"]
    print(Solution().minExtraChar(s, dictionary))