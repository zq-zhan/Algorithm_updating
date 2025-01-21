# 20250116——或值至少k的最短子数组1
class Solution1:
	def minimumSubarrayLength(self, nums, k):
		ans = len(nums) + 1
		left = 0
		temp = []
		temp_ori = 0
		for right, c in enumerate(nums):
			temp.append(c)
			for x in temp:
				temp_ori != x 
			while temp_ori >= k:
				ans = min(ans, right - left + 1)
				temp = temp[1:]
				left += 1
		return ans
	
## 灵神题解
class Solution2:
	def minimumSubarrayLength(self, nums, k):
		ans = len(nums) + 1
		left = bottom = right_or = 0
		for right, x in enumerate(nums):
			right_or |= x
			while left <= right and nums[left] | right_or >= k:
				ans = min(ans, right - left + 1)
				left += 1
				if bottom < left:
					# 构建一个栈
					for i in range(right - 1, left - 1, -1):
						nums[i] |= nums[i + 1]
					bottom = right
					right_or = 0
		return ans if ans <= len(nums) else -1
	
if __name__ == '__main__':
	nums = [1,2,3]
	k = 2
	cls = Solution2()
	print(cls.minimumSubarrayLength(nums, k))
