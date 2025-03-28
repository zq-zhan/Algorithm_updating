

# 9.卡车上的最大单元数
class Solution1:
	def maximumUnits(self, boxTypes, truckSize):
		boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
		ans = 0
		for box_num, value in boxTypes:
			for _ in range(box_num):
				truckSize -= 1
				ans += value
				if truckSize == 0:
					return ans
				
## 优化
class Solution2:
	def maximumUnits(self, boxTypes, truckSize):
		boxTypes = sorted(boxTypes, key = lambda x: -x[1])
		ans = 0
		for box_num, value in boxTypes:
			if box_num > truckSize:
				ans += truckSize * value
				return ans
			else:
				truckSize -= box_num
				ans += value * box_num
		return ans

if __name__ == '__main__':
	boxTypes = [[1,3],[2,2],[3,1]]
	truckSize = 4
	print(Solution2().maximumUnits(boxTypes, truckSize))