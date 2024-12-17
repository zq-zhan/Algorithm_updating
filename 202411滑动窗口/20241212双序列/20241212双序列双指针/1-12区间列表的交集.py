# 12.区间列表的交集
class Solution1:
	def intervalIntersection(self,firstList,secondList):
		n, m = len(firstList), len(secondList)
		if len(firstList)==0 or len(secondList)==0:
			return []
		p1 = p2 = 0
		ans = []
		while p1 < n and p2 < m:
			if firstList[p1][1] < secondList[p2][0]:
				p1 += 1
				continue
			elif firstList[p1][0] > secondList[p2][1]:
				p2 += 1
				continue
			else:
				temp_list=[]
				if firstList[p1][1] < secondList[p2][1]:
					max_p1_num = max(firstList[p1][0],secondList[p2][0])
					# for i in range(max_p1_num,firstList[p1][1]+1):
					# 	temp_list.append(i)
					ans.append([max_p1_num,firstList[p1][1]])
					p1 += 1
				else:
					max_p1_num = max(firstList[p1][0],secondList[p2][0])
					# for i in range(max_p1_num,secondList[p2][1]):
					# 	temp_list.append(i)
					ans.append([max_p1_num,secondList[p2][1]])
					p2 += 1
		return ans
	
## 优化
class Solution2:
	def intervalIntersection(self,firstList,secondList):
		p1 = p2 = 0
		n, m = len(firstList),len(secondList)
		ans = []
		while p1 < n and p2 < m:
			a1, a2 = firstList[p1][0],firstList[p1][1]
			b1, b2 = secondList[p2][0], secondList[p2][1]
			if a1 <= b2 and a2 >= b1:
				ans.append([max(a1,b1),min(a2,b2)])
			if b2 < a2:
				p2 += 1
			else:
				p1 += 1
		return ans
	
if __name__ == '__main__':
	firstList = [[0,2],[5,10],[13,23],[24,25]]
	secondList = [[1,5],[8,12],[15,24],[25,26]]
	s = Solution2()
	print(s.intervalIntersection(firstList,secondList))