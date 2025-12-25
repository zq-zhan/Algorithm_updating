from collections import defaultdict

class Solution:
	def minSubarray(self, nums, p):
		pre_s = 0
		ans = len(nums)
		temp_dic = defaultdict(int)
		temp_dic[0] = -1
		for i, x in enumerate(nums):
			pre_s += x
			if pre_s % p in temp_dic:
				ans = min(ans, i - temp_dic[pre_s % p])
			temp_dic[pre_s % p] = i
		return ans if ans < len(nums) else -1

if __name__ == '__main__':
	nums = [3,1,4,2]
	p = 6
	print(Solution().minSubarray(nums, p))