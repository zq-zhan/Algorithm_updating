# 4.特殊数组2
from itertools import accumulate, pairwise


class Solution1:
	def isArraySpecial(self, nums, queries):
		pre_lis = [0, 1]
		for p1 in range(1, len(nums)):
			if nums[p1] % 2 != nums[p1 - 1] % 2:
				pre_lis.append(pre_lis[-1] + 1)
			else:
				pre_lis.append(pre_lis[-1] - 1)
		ans = []
		for left, right in queries:
			if right - left == 0:
				ans.append(False)
			elif pre_lis[right + 1] - pre_lis[left] == right - left + 1:
				ans.append(True)
			else:
				ans.append(False)
		return ans
## 灵神题解
class Solution2:
	def isArraySpecial(self, nums, queries):
		a_lis = []  # 长度为n - 1
		for p1 in range(len(nums)):
			if nums[p1] % 2 != nums[p1 + 1] % 2:
				a_lis.append(0)
			else:
				a_lis.append(-1)
		pre_a_sum = [0]
		for x in a_lis:
			pre_a_sum.append(pre_a_sum[-1] + x)

		ans = []
		for left, right in queries:
			if pre_a_sum[right] == pre_a_sum[left]:
				ans.append(True)
			else:
				ans.append(False)
		return ans
class Solution3:
	def isArraySpecial(self, nums, queries):
		s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), intial = 0))
		return [s[right] == s[left] for left, right in queries]


if __name__ == '__main__':
	nums = [3,4,1,2,6]
	queries = [[0,4]]
	cls = Solution3()
	print(cls.isArraySpecial(nums, queries))