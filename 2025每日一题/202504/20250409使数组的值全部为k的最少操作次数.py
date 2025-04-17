# 20250409使数组的值全部为k的最少操作次数
class Solution1:
	def minOperations(self, nums, k):
		if min(nums) != k:
			return -1
		return len(set(nums)) - 1

## 指针
class Solution2:
	def minOperations(self, nums, k):
		nums = list(set(nums))
		nums.sort(reverse = True)
		if nums[-1] < k:
			return -1
		ans = 0
		for i, c in enumerate(nums):
			if c > k:
				ans += 1
		return ans

if __name__ == '__main__':
	nums = [2,1,2]
	k = 2
	print(Solution2().minOperations(nums, k))