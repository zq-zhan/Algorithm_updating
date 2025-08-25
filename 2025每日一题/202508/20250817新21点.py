from functools import cache

# class Solution:
# 	def new21Game(self, n, k, maxPts):
# 		res = []
# 		@cache
# 		def dfs(path_s):
# 			if path_s >= k:
# 				res.append(path_s)
# 				return 
# 			for x in range(1, maxPts + 1):
# 				dfs(path_s + x)
# 		dfs(0)
# 		pos = 0
# 		for x in res:
# 			pos += int(x <= n)
# 		return pos/len(res)
	
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp=[None]*(K+W)
        s=0
        for i in range(K,K+W):          # 填蓝色的格子
            dp[i] = 1 if i<=N else 0
            s+=dp[i]
        for i in range(K-1,-1,-1):      # 填橘黄色格子
            dp[i]=s/W
            s=s-dp[i+W]+dp[i]
        return dp[0]

if __name__ == '__main__':
	n = 21
	k = 17
	maxPts = 10
	print(Solution().new21Game(n, k, maxPts))