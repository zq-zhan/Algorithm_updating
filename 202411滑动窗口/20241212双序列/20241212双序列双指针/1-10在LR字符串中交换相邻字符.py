from collections import Counter

# 10.在LR字符串中交换相邻字符
class Solution1:
	def canTransform(self,start,result):
		start_dic=Counter(start)
		result_dic=Counter(result)
		if start_dic != result_dic:
			return False
		i = 0
		j = 0 
		while i < len(start)-1:
			if start[i]==result[j+1] and start[i+1]==result[j] and (start[i]=='X' or start[i+1]=='X'):
				j += 2
				i += 2
				continue
			if start[i]==result[j]:
				i += 1
				j += 1
			else:
				return False
		return True
## 灵神思路
class Solution2:
	def canTransform(self,start,result):
		if start.replace('X','')!=result.replace('X',''):
			return False
		j = 0
		for i,c in enumerate(start):
			if start[i] == 'X':
				continue
			while result[j]=='X':
				j += 1
			if i!=j and (c == 'L') == (i < j):
				return False
			j += 1
		return True

	
if __name__ == '__main__':
	start = "LXXLXRLXXL"
	result = "XLLXRXLXLX"
	s = Solution2()
	print(s.canTransform(start,result))