from itertools import accumulate

class Solution:
	def platesBetweenCandles(self, s, queries):
		n = len(s)  # 二分找左右两边第一个符合条件序号，再利用前缀和计算
		caddles = []
		for i, x in enumerate(s):
			if x == '|':
				caddles.append(i)
		s = [1 if x == '*' else 0 for x in s ]
		pre_s = list(accumulate(s, initial = 0))
		ans = []
		for left, right in queries:
			left_new = bisect_left(caddles, left)
			right_new = bisect_right(caddles, right) - 1
			diff = pre_s[right] - pre_s[left]
			if left_new < n and right_new >= 0 and left_new < right_new:
				ans.append(pre_s[caddles[right_new]] - pre_s[caddles[left_new]])
			else:
				ans.append(0)
			# while left < right and pre_s[left] != pre_s[left + 1]:  # 超时
			# 	left += 1
			# while left < right and pre_s[right] != pre_s[right + 1]:
			# 	right -= 1
			# ans.append(pre_s[right] - pre_s[left])
		return ans

	
if __name__ == '__main__':
	s = "***|**|*****|**||**|*"
	queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
	print(Solution().platesBetweenCandles(s, queries))
