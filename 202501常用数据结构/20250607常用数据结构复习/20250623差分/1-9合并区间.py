from itertools import accumulate

class Solution:
	def merge(self, intervals):
		mx = max(end for _, end in intervals)
		new_arr = [0] * (mx + 2)
		for start, end in intervals:
			new_arr[start] += 1
			new_arr[end] -= 1

		pre_s = list(accumulate(new_arr))
		ans = []
		left = -1
		for i, x in enumerate(pre_s):
			if x == 0 and i > 0 and i - left > 1:
				ans.append([left + 1, i])
			if x == 0:
				left = i
		return ans


	
if __name__ == '__main__':
	intervals = [[1,4],[5,6]]
	print(Solution().merge(intervals))