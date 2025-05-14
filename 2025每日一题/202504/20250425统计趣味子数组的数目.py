# 20250425统计趣味子数组的数目
class Solution1:
	def countInterestingSubarrays(self, nums, modulo, k):
		cnt = 0
		left = ans = 0
		for right, c in enumerate(nums):
			cnt += 1 if c % modulo == k else 0
			while cnt % modulo == k:
				cnt -= 1 if nums[left] % modulo == k else 0
				left += 1
			ans += left
		return ans

if __name__ == '__main__':
	# nums = [3,2,4]
	nums = [3,1,9,6]
	modulo = 3
	k = 0
	print(Solution1().countInterestingSubarrays(nums, modulo, k))