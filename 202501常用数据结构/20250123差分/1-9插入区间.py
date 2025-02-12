# 9.插入区间
class Solution1:
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)
		intervals.sort()

		ans = []
		for left, right in intervals:
			if ans and ans[-1][1] >= left:
				ans[-1][1] = max(ans[-1][1], right)
			else:
				ans.append([left, right])
		return ans
## 一次遍历思路
class Solution2:
	def insert(self, intervals, newInterval):
		n_start, n_end = newInterval
		ans = []

		for start, end in intervals:
			if end < n_start or start > n_end:
				ans.append([start, end])
				continue
			n_start = min(n_start, start)
			n_end = max(n_end, end)
		ans.append([n_start, n_end])
		ans.sort()
		return ans
	
if __name__ == '__main__':
	intervals = [[1,3],[6,9]]
	newInterval = [2,5]
	cls = Solution2()
	print(cls.insert(intervals, newInterval))