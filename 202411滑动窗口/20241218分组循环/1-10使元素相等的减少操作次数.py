# 10.使元素相等的减少操作次数
class Solution1:
	def reductionOperations(self,nums):
		nums.sort()
		ans = i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			while nums[i] == nums[i - 1]:
				i += 1
			nums[i] = nums[i - 1]
			ans += i - start
		return ans
	
class Solution2:
	def reductionOperations(self,nums):
		nums.sort()
		ans = cnt = 0
		n = len(nums)
		i = 0
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] == nums[i - 1]:
				i += 1
			ans += (i - start) * cnt
			cnt += 1
		return ans
	
if __name__ == '__main__':
	nums = [1,1,2,2,3]
	cls = Solution2()
	print(cls.reductionOperations(nums))