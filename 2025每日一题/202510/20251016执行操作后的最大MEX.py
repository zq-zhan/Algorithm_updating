from collections import Counter

class Solution:
	def findSmallestInteger(self, nums, value):
		cnt = Counter(x % value for x in nums)
		ans = 0
		while cnt[ans % value]:
			cnt[ans % value] -= 1
			ans += 1
		return ans

		
			
if __name__ == '__main__':
	nums = [0,0,-4,-4,2,2,3,3,4,4]
	value = 5
	print(Solution().findSmallestInteger(nums, value))