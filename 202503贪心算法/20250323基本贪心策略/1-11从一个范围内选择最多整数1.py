# 11.从一个范围内选择最多整数1
class Solution1:
	def maxCount(self, banned, n, maxSum):
		ans = 0
		banned = list(set(banned))
		banned.sort()
		p1 = 0
		for x in range(1, n + 1):
			if p1 >= len(banned) or x != banned[p1]:
				maxSum -= x
				ans += 1
				if maxSum == 0:
					return ans
				elif maxSum < 0:
					return ans - 1
			else:
				p1 += 1
		return ans

	
if __name__ == '__main__':
	banned = [87,193,85,55,14,69,26,133,171,180,4,8,29,121,182,78,157,53,26,7,117,138,57,167,8,103,32,110,15,190,139,16,49,138,68,69,92,89,140,149,107,104,2,135,193,87,21,194,192,9,161,188,73,84,83,31,86,33,138,63,127,73,114,32,66,64,19,175,108,80,176,52,124,94,33,55,130,147,39,76,22,112,113,136,100,134,155,40,170,144,37,43,151,137,82,127,73]
	n = 1079
	maxSum = 87
	print(Solution1().maxCount(banned, n, maxSum))