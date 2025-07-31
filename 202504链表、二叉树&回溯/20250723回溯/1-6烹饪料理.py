class Solution:
	def perfectMenu(self, material, cookbooks, attribute, limit):
		ans = -1
		n = len(cookbooks)
		m = len(cookbooks[0])
		path = [0] * m
		def dfs(i, temp_x, temp_y):
			nonlocal ans
			if i == n:
				if temp_y >= limit:
					ans = max(ans, temp_x)
				return 
			dfs(i + 1, temp_x, temp_y)
			if all(path[j] + cookbooks[i][j] <= material[j] for j in range(m)):
				temp_x += attribute[i][0]
				temp_y += attribute[i][1]
				for j in range(m):
					path[j] += cookbooks[i][j]
				dfs(i + 1, temp_x, temp_y)
				for j in range(m):
					path[j] -= cookbooks[i][j]
		dfs(0, 0, 0)
		return ans
	
if __name__ == '__main__':
	material = [3,2,4,1,2]
	cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
	attribute = [[3,2],[2,4],[7,6]]
	limit = 5
	s = Solution()
	print(s.perfectMenu(material, cookbooks, attribute, limit))