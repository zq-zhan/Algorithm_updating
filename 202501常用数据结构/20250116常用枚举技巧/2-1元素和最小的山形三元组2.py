# 枚举中间变量
from math import inf

# 1.元素和最小的山形三元组
class Solution1:
	def minimumSum(self, nums):
		n = len(nums)
		ans = inf
		for j in range(1, n - 1):
			left = right = mid = nums[j]
			i = j - 1
			k = j + 1

			while i >= 0 and k < n:
				if nums[i] >= left:
					i -= 1
					continue
				if nums[k] >= right:
					k += 1
					continue
				left = nums[i]
				right = nums[k]
				ans = min(ans, left + mid + right)
		return ans if ans < inf else -1
	
## 灵神题解
class Solution2:
	def minimumSum(self, nums):
		n = len(nums)
		suf = [0] * n
		suf[-1] = nums[-1]
		for i in range(n - 2, 1, -1):
			suf[i] = min(suf[i + 1], nums[i])

		ans = inf
		pre = nums[0]
		for j in range(1, n - 1):
			if pre < nums[j] > suf[j + 1]:
				ans = min(ans, pre + nums[j] + suf[j + 1])
			pre = min(pre, nums[j])
		return ans if ans < inf else -1
	
if __name__ == '__main__':
	nums = [8,6,1,5,3]
	cls = Solution2()
	print(cls.minimumSum(nums)) # Output: 16