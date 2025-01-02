# 18.最长交替子数组
class Solution1:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			flag = 1
			while i < n and nums[i] - nums[i - 1] == flag:
				i += 1
				flag *= (-1)
			if i - start > 1:
				ans = max(ans, i - start)
			if i < n:
				i = start + 1
			else:
				break
		return ans

## 灵神思路
class Solution2:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n - 1:
			if nums[i + 1] - nums[i] != 1:
				i += 1
				continue
			start = i
			i += 2
			while i < n and nums[i] == nums[i - 2]:
				i += 1
			ans = max(ans, i - start)
			i -= 1
		return ans
	
## 优化
class Solution3:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			if start < n - 1 and nums[start + 1] - nums[start] != 1:
				# i += 1
				continue
			elif start == n - 1:
				break
			flag = 1
			while i < n and nums[i] - nums[i - 1] == flag:
				i += 1
				flag *= (-1)
			ans = max(ans, i - start)
			i -= 1
		return ans

if __name__ == '__main__':
	nums = [21,9,5]
	cls = Solution1()
	print(cls.alternatingSubarray(nums))