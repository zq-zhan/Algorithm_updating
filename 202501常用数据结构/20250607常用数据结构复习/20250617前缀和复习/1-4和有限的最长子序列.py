class Solution:
	def answerQueries(self, nums, queries):
		nums.sort()
		pre_s = [0] 
		for x in nums:
			pre_s.append(pre_s[-1] + x)

		ans = []
		for querie in queries:
			for i, temp_s in enumerate(pre_s):
				if temp_s > querie:
					ans.append(i - 1)
					break
				elif i == len(nums):
					ans.append(i)
		return ans
	
## 前缀和+二分查找
class Solution:
	def answerQueries(self, nums, queries):
		# def find(target):  # >=x二分查找标准写法
		# 	left, right = -1, len(nums)
		# 	while left + 1 < right:
		# 		mid = (left + right) // 2
		# 		if pre_s[mid] >= target:
		# 			right = mid
		# 		else:
		# 			left = mid
		# 	return right
		nums.sort()
		for i in range(1, len(nums)):
			nums[i] += nums[i - 1] 

		ans = []
		for querie in queries:
			# ans.append(find(querie + 1))  # >x的元素序号作为<=x的元素个数
			ans.append(bisect_right(nums, querie))
		return ans


if __name__ == '__main__':
	nums = [4,5,2,1]
	queries = [3,10,21]
	print(Solution().answerQueries(nums, queries))