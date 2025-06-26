from itertools import accumulate

class Solution:
	def isCovered(self, ranges, left, right):
		mx = max(end for _, end in ranges)
		if left > mx:
			return False
		new_arr = [0] * (mx + 2)
		for start, end in ranges:
			new_arr[start] += 1
			new_arr[end + 1] -= 1
		pre_s = list(accumulate(new_arr))
		return all(x > 0 for x in pre_s[left:right + 1])
	
if __name__ == '__main__':
	ranges = [[1,1]]
	left = 50
	right = 50
	print(Solution().isCovered(ranges, left, right))