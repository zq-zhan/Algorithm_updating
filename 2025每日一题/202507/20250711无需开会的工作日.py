from itertools import accumulate

class Solution:  
	def countDays(self, days, meetings):
		new_arr = [[1, 0]]
		meetings.sort(key = lambda x:x[0])
		ans = 0
		n = len(meetings)
		for i in range(n):
			ans += max(0, meetings[i][0] - new_arr[-1][1] - 1)
			if meetings[i][0] <= new_arr[-1][1] + 1:
				new_arr[-1][1] = max(meetings[i][1], new_arr[-1][1])
			else:
				new_arr.append(meetings[i])
		ans += max(0, days - new_arr[-1][1])
		return ans
	
if __name__ == '__main__':
	days = 8
	meetings = [[3,4], [4,8], [2,5],[3,8]]
	print(Solution().countDays(days, meetings))