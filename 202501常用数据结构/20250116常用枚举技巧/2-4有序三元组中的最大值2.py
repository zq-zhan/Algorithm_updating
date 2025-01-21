class Solution1:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		suf = [nums[-1]] * n
		for p1 in range(n - 2, -1, -1):
			suf[p1] = max(nums[p1], suf[p1 + 1])
		pre = [nums[0]] * n
		for p2 in range(1, n):
			pre[p2] = max(nums[p2], pre[p2 - 1])

		for j in range(1, n - 1):
			ans = max(ans, (pre[j - 1] - nums[j]) * suf[j + 1])
		return ans
	
## 灵神题解——优化思路：前缀最大值可以在计算答案的同时算出来
class Solution2:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		suf_max = [0] * (n + 1)
		for p1 in range(n - 1, 1, -1):
			suf_max[p1] = max(suf_max[p1 + 1], nums[p1])
		pre_max = 0
		for j, x in enumerate(nums):
			ans = max(ans, (pre_max - x) * suf_max[j + 1])
			pre_max = max(pre_max, x)
		return ans

if __name__ == '__main__':
	nums = [12,6,1,2,7]
	cls = Solution1()
	print(cls.maximumTripletValue(nums))