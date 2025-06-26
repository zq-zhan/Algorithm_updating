from collections import defaultdict
from bisect import bisect_left

class Solution1:
	def solveQueries(self, nums, queries):
		nums_cnt = defaultdict(list)
		for i, c in enumerate(nums):
			nums_cnt[c].append(i)

		n = len(queries)
		ans = [-1] * n
		for i, x in enumerate(queries):
			temp = nums_cnt[nums[x]].copy()
			p0 = temp[0]
			temp.insert(0, temp[-1] - len(nums))
			temp.append(p0 + len(nums))
			m = len(temp)
			if m > 3:
				j = bisect_left(temp, x)
				ans[i] = min(x - temp[j - 1], temp[j + 1] - x)
		return ans

## 灵神题解
class Solution2:
	def solveQueries(self, nums, queries):
		nums_cnt = defaultdict(list)
		for i, x in enumerate(nums):
			nums_cnt[x].append(i)

		n = len(nums)
		for p in nums_cnt.values():
			i0 = p[0]
			p.insert(0, p[-1] - n)  # 前后哨兵
			p.append(i0 + n)

		for qi, i in enumerate(queries):
			p = nums_cnt[nums[i]]
			if len(p) == 3:
				queries[qi] = -1
			else:
				j = bisect_left(p, i)
				queries[qi] = min(i - p[j - 1], p[j + 1] - i)
		return queries


	
if __name__ == '__main__':
	nums = [18,7,7,7,18,7,18,18,7,7,2,17,7,4]
	queries = [2,3,1,6,12,9,5,13]
	print(Solution2().solveQueries(nums, queries))