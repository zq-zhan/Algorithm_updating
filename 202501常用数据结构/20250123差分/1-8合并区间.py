# 8.合并区间
class Solution1:
	def merge(self, intervals):
		intervals.sort(key = lambda x: x[0])

		ans = []
		for left, right in intervals:
			if ans and left <= ans[-1][1]:
				ans[-1][1] = max(right, ans[-1][1])
			else:
				ans.append([left, right])
		return ans
	
if __name__ == '__main__':
	intervals = [[1,3],[2,6],[8,10],[15,18]]
	cls = Solution1()
	print(cls.merge(intervals))