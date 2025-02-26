# 4.人口最多的年份
from itertools import accumulate
from collections import defaultdict


class Solution1:
	def maximumPopulation(self, logs):
		d = [0] * (100 + 2)
		for birth, death in logs:
			d[birth - 1950 + 1] += 1
			d[death - 1950 + 1] -= 1

		ans = 2051
		temp_s = 0
		for i, s in enumerate(list(accumulate(d))):
			# temp_s += s
			if s > temp_s:
				temp_s = s
				ans = i + 1949
		return ans
	
## 方法二
class Solution2:
	def maximumPopulation(self, logs):
		d = defaultdict(int)
		for birth, death in logs:
			d[birth] += 1
			d[death] -= 1

		ans = 2051
		temp_s = max_s = 0
		for year, s in sorted(d.items()):
			temp_s += s
			if max_s < temp_s:
				max_s = temp_s
				ans = year
		return ans

				
if __name__ == '__main__':
	logs = [[1950,1961],[1960,1971],[1970,1981]]
	print(Solution1().maximumPopulation(logs)) # 1993