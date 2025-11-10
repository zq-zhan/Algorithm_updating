from collections import defaultdict
from math import inf
import heapq

class NumberContainers:

	def __init__(self):
		self.target_dic = defaultdict(list)
		self.target_idx = defaultdict(int)

	def change(self, index: int, number: int):
		self.target_idx[index] = number
		heapq.heappush(self.target_dic[number], index)

	def find(self, number: int): 
		temp = self.target_dic[number]
		while temp and self.target_idx[temp[0]] != number:
			heapq.heappop(temp)  # 旧数据可以直接删除
		return temp[0] if temp else -1
			
if __name__ == '__main__':
	s = NumberContainers()
	
	s.change(1, 10)
	print(s.find(10)) 
	s.change(1, 20)
	print(s.find(10)) 
	print(s.find(20))
	print(s.find(30))  
