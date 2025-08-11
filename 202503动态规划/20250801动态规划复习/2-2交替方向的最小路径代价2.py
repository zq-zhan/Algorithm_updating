from functools import cache
from math import inf

class Solution:
    def minCost(self, m, n, waitCost):
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return 1  # 起点只有进入成本，不需要等待
            return min(dfs(i, j - 1), dfs(i - 1, j)) + waitCost[i][j] + (i + 1) * (j + 1)
        return dfs(m - 1, n - 1) - waitCost[-1][-1]  # 终点不需要等待

    
if __name__ == '__main__':
    m = 2
    n = 2
    waitCost = [[3,5],[2,4]]
    print(Solution().minCost(m, n, waitCost))