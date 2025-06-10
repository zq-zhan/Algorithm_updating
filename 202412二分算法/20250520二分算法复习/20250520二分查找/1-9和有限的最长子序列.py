class Solution1:
	def answerQueries(self, nums, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		nums.sort()
		for i in range(1, len(nums)):
			nums[i] = nums[i] + nums[i - 1]

		ans = []
		for x in queries:
			ans.append(lower_bound(nums, x + 1))
		return ans
	
if __name__ == '__main__':
	nums = [4,5,2,1]
	queries = [3,10,21]
	print(Solution1().answerQueries(nums, queries))