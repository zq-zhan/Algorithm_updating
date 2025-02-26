# 1.使数组元素全部相等的最少操作次数
from itertools import accumulate
from bisect import bisect_left

class Solution1:
	def minOperations(self, nums, queries):
		ans = [0] * len(queries)
		for i, querie in enumerate(queries):
			ans[i] += sum(abs(x - querie) for x in nums)

		return ans

## 灵神题解
class Solution2:
	def minOperations(self, nums, queries):
		n = len(nums)
		nums.sort()
		s = list(accumulate(nums, initial = 0))  # 前缀和
		ans = []
		for q in queries:
			j = bisect_left(nums, q)
			left = q * j - s[j]
			right = s[n] - s[j] - q * (n - j)
			ans.append(left + right)
		return ans


if __name__ == '__main__':
    nums = [3,1,6,8]
    queries = [1,5]
    cls = Solution2()
    print(cls.minOperations(nums, queries))