# 16.使绳子变成彩色的最短时间
class Solution1:
	def minCost(self,colors,neededTime):
		i = 0
		n = len(colors)
		ans = 0
		while i < n:
			start = i
			i += 1
			while i < n and colors[i] == colors[i - 1]:
				i += 1
			if i - start > 1:
				remove_lis = sorted(neededTime[start:i])
				ans += sum(remove_lis[:-1])
		return ans
	
if __name__ == '__main__':
	colors = "abaac"
	neededTime = [1,2,3,4,5]
	cls = Solution1()
	print(cls.minCost(colors,neededTime))