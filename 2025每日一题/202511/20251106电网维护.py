from collections import defaultdict
from math import inf

## 错解
class Solution:
	def processQueries(self, c, connections, queries):
		new_dic = defaultdict(list)
		for x, y in connections:
			new_dic[x].append(y)
			new_dic[y].append(x)

		ans = []
		remove_set = set()
		for tag, x in queries:
			if tag == 1:
				if x not in remove_set:
					ans.append(x)
					continue
				else:
					temp_lis = new_dic[x]
					temp_tag = False
					if temp_lis:
						temp_lis.sort()
						for y in temp_lis:
							if y not in remove_set:
								ans.append(y)
								temp_tag = True
								break
					if not temp_tag:
						ans.append(-1)
			else:
				remove_set.add(x)
		return ans
## 灵神题解
class Solution:
    def processQueries(self, c, connections, queries):
        g = [[] for _ in range(c + 1)]
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        cc = 0  # 连通块编号

        def dfs(x: int) -> None:
            belong[x] = cc  # 记录节点 x 在哪个连通块
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] < 0:
                dfs(i)
                cc += 1

        # 记录每个节点的离线时间，初始为无穷大（始终在线）
        offline_time = [inf] * (c + 1)
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            if t == 2:
                offline_time[x] = i  # 记录离线时间

        # 每个连通块中仍在线的电站的最小编号
        mn = [inf] * cc
        for i in range(1, c + 1):
            if offline_time[i] == inf:  # 最终仍在线
                j = belong[i]
                mn[j] = min(mn[j], i)

        ans = []
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            j = belong[x]
            if t == 2:
                if offline_time[x] == i:
                    mn[j] = min(mn[j], x)  # 变回在线
            elif i < offline_time[x]:  # 已经在线（写 < 或者 <= 都可以）
                ans.append(x)
            elif mn[j] != inf:
                ans.append(mn[j])
            else:
                ans.append(-1)
        ans.reverse()
        return ans





	
if __name__ == '__main__':
	c = 4
	connections = [[4,3],[3,1],[4,2],[3,2],[4,1]]
	queries = [[2,3],[1,2],[2,4],[1,1],[2,2],[1,2],[1,2],[2,2],[1,3],[2,3],[2,4],[2,3],[2,4],[1,2],[1,1]]
	print(Solution().processQueries(c, connections, queries))