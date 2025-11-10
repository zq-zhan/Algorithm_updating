class Solution:
	def getSneakyNumbers(self, nums):
		n = len(nums) - 2
		new_arr = [0] * n
		ans = []
		for x in nums:
			if new_arr[x]:
				ans.append(x)
			if len(ans) == 2:
				return ans
			new_arr[x] += 1
# 空间O(1)做法
class Solution:
	def getSneakyNumbers(self, nums):
		n = len(nums)
		k = n - 2
		while k < n:
			x = nums[k]
			if nums[x] == x:
				k += 1
				continue
			nums[k], nums[x] = nums[x], nums[k]
		return nums[-2:]


if __name__ == '__main__':
	nums = [0,3,2,1,3,2]
	print(Solution().getSneakyNumbers(nums))