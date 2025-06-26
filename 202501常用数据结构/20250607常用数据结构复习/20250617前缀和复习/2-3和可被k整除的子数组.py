from collections import defaultdict

class Solution:
	def subarraysDivByK(self, nums, k):
		dic_win = defaultdict(int)
		ans = temp_s = 0
		dic_win[0] = 1
		for x in nums:
			temp_s += x
			ans += dic_win[k - temp_s % k]
			dic_win[x % k] += 1
		return ans
	
if __name__ == '__main__':
	nums = [4,5,0,-2,-3,1]
	k = 5
	print(Solution().subarraysDivByK(nums, k))