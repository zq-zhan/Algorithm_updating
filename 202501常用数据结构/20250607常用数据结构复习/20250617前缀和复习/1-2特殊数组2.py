class Solution:  # 错解
	def isArraySpecial(self, nums, queries):
		suf_s = [0] * (len(nums) + 1)
		for i, x in enumerate(nums):
			suf_s[i + 1] = suf_s[i] + nums[i]

		ans = []
		for start, end in queries:
			ans.append((suf_s[end + 1] - suf_s[start]) % 2 == 1)
		return ans
	
## 灵神思路
class Solution:
	def isArraySpecial(self, nums, queries):
		a = []
		n = len(nums)
		for i in range(n - 1):
			if nums[i] % 2 != nums[i + 1] % 2:
				a.append(0)
			else:
				a.append(1)
		suf_s = list(accumulate(a, initial = 0))
		ans = []
		for start, end in queries:
			if suf_s[end] - suf_s[start] == 0:
				ans.append(True)
			else:
				ans.append(False)
		return ans 
	
if __name__ == '__main__':
	nums = [4,3,1,6]
	queries = [[0,2],[2,3]]
	print(Solution().isArraySpecial(nums, queries))