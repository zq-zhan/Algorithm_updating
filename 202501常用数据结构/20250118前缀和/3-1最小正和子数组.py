# 前缀和与有序集合
from itertools import accumulate
from sortedcontainers import SortedList
from math import inf

# 1.最小正和子数组
# class Solution1:
# 	def minimumSumSubarray(self, nums, l, r):
# 		pre_sum = [nums[0]]
# 		for i in range(1, len(nums)):
# 			pre_sum.append(pre_sum[-1] + nums[i])

# 		ans = sum(nums)
# 		cnt = {0:-1}
# 		for j, sj in enumerate(nums):
# 			i = cnt.get(sj, j)
# 			if i == j:
# 				cnt[sj % ]
## 灵神题解
class Solution2:
	def minimumSumSubarray(self, nums, l, r):
		ans = inf
		s = list(accumulate(nums, initial = 0))
		sl = SortedList()
		for j in range(l, len(nums) + 1):
			sl.add(s[j - l])
			k = sl.bisect_left(s[j])  # 找到第一个>=s[j]元素的索引，那么s[k - 1]就是与s[j]值最接近的s[i]
			if k:  # 当k不为0时，说明sl中存在这样的s[i]
				ans = min(ans, s[j] - sl[k - 1])
			if j >= r:  # 使下一个j时，i要满足 j - r <= i <= j - l
				sl.remove(s[j - r])
		return -1 if ans == inf else ans
	
if __name__ == '__main__':
	nums = [3,-2,1,4]
	l, r = 2,2
	print(Solution2().minimumSumSubarray(nums, l, r))