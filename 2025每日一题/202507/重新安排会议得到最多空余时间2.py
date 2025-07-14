class Solution:
	def maxFreeTime(self, eventTime, startTime, endTime):
		n = len(startTime)
		free = [0] * (n + 1)
		free[0] = startTime[0]  # 最左边的空余时间段
		for i in range(1, n):
			free[i] = startTime[i] - endTime[i - 1]
		free[n] = eventTime - endTime[-1]

		ans = s = 0
		for i, f in enumerate(free):
			s += f
			if i < 2:
				continue
			ans = max(ans, s)
			s -= free[i - 2]
		return ans

if __name__ == '__main__':
	eventTime = 10
	startTime = [0,3,7,9]
	endTime = [1,4,8,10]
	print(Solution().maxFreeTime(eventTime, startTime, endTime))
	