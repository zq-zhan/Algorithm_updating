# 2.装满石头的背包的最大数量
class Solution1:
	def maximumBags(self, capacity, rocks, additionalRocks):
		capacity = [x - y for x, y in zip(capacity, rocks)]
		capacity.sort()
		for i, x in enumerate(capacity, 1):
			additionalRocks -= x
			if additionalRocks == 0:
				return i
			elif additionalRocks < 0:
				return i - 1
		return i

## 写法二
class Solution2:
	def maximumBags(self, capacity, rocks, additionalRocks):
		capacity = [x - y for x, y in zip(capacity, rocks)]
		capacity.sort()
		ans = 0
		while additionalRocks >= 0:
			additionalRocks -= capacity[ans]
			ans += 1
		return ans if additionalRocks == 0 else ans - 1
			
if __name__ == '__main__':
	capacity = [91,54,63,99,24,45,78]
	rocks = [35,32,45,98,6,1,25]
	additionalRocks = 17
	print(Solution2().maximumBags(capacity, rocks, additionalRocks))