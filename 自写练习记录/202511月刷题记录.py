# 20251101从链表中移除在数组中存在的节点
class Solution:
	def modifiedList(self, nums, head):
		num_node = ListNode(0, next = head)
		cur = num_node
		nums = set(nums)
		while cur:
			if cur.next and cur.next.val in nums:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return num_node.next

# 20251102统计网格图中没有被保卫的格子数
## 灵神题解
DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)
class Solution:
	def countUnguarded(self, m, n, guards, walls):
		guarded = [[0] * n for _ in range(m)]

		for x, y in guards:
			guarded[x][y] = -1
		for x, y in walls:
			guarded[x][y] = -1

		# 遍历警卫
		for x0, y0 in guards:
			for dx, dy in DIRS:
				x, y = x0 + dx, y0 + dy
				while 0 <= x < m and 0 <= y < n and guarded[x][y] != -1:
					guarded[x][y] = 1 # 被保卫
					x += dx
					y += dy

		return sum(row.count(0) for row in guarded)

# 20251103使绳子变成彩色的最短时间
class Solution:
	def minCost(self, colors, neededTime):
		ans = 0
		n = len(colors)
		for i in range(1, n):
			if colors[i] == colors[i - 1]:
				if neededTime[i] < neededTime[i - 1]:
					ans += neededTime[i]
					neededTime[i] = neededTime[i - 1]
				else:
					ans += neededTime[i - 1]
		return ans

# 20251104计算子数组的x-sum
class Solution:
	def findXSum(self, nums, k, x):
		temp_dic = defaultdict(int)
		ans = []
		for i, num in enumerate(nums):
			temp_dic[num] += 1
			if sum(temp_dic.values()) < k:
				continue
			else:
				new_arr = [(cnt, key) for key, cnt in temp_dic.items()]
				new_arr.sort(reverse = True)
				temp_s = 0
				for j in range(min(x, len(new_arr))):
					temp_s += new_arr[j][0] * new_arr[j][1]
				ans.append(temp_s)
				temp_dic[nums[i - k + 1]] -= 1	
		return ans		

# 20251106电网维护
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














