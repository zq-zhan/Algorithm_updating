from collections import defaultdict

class Solution:
	def beautifulSubarrays(self, nums):
		ans = s = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		for x in nums:
			s ^= x
			ans += cnt[s]
			cnt[s] += 1
		return ans

class Solution:
	def beautifulSubarrays(self, nums):
		ans = s = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		for x in nums:
			s ^= x
			ans += cnt[s % 2]
			cnt[s % 2] += 1
		return ans
		
if __name__ == '__main__':
	nums = [4,3,1,2,4]
	print(Solution().beautifulSubarrays(nums))