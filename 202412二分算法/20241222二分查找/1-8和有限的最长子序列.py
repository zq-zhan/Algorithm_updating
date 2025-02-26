# 8.和有限的最长子序列
from bisect import bisect_left,bisect_right


class Solution1:
	def answerQueries(self,nums,queries):
		ans = []
		new_arr = [0] * len(nums)
		nums.sort()
		for i,x in enumerate(nums):
			if i == 0:
				new_arr[i] = nums[i]
			else:
				new_arr[i] = nums[i] + new_arr[i - 1]
		for i in range(len(queries)):
			find = bisect_left(new_arr,queries[i] + 1) - 1
			# if find == -1:
			# 	ans.append(0)
			# else:
			# 	ans.append(find + 1)
			ans.append(find + 1)
		return ans
	
class Solution2:
	def answerQueries(self,nums,queries):
		def lower_bound(nums, target):  # 找到>=target的最小序号
			left, right = -1, len(nums) 
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		nums.sort()
		for i in range(1, len(nums)):
			nums[i] = nums[i] + nums[i - 1]
		ans = []
		for x in queries:
			find = lower_bound(nums, x + 1) - 1
			if find == -1:
				ans.append(0)
			else:
				ans.append(find + 1)
		return ans
	
class Solution3:
	def answerQueries(self, nums, queries):
		nums.sort()
		new_nums = [nums[0]]
		for i in range(1, len(nums)):
			new_nums.append(new_nums[-1] + nums[i])

		ans = []
		for x in queries:
			ans.append(bisect_right(new_nums, x))
		return ans


if __name__ == '__main__':
	nums = [2,3,4,5]
	queries = [1]
	cls = Solution3()
	print(cls.answerQueries(nums,queries))
