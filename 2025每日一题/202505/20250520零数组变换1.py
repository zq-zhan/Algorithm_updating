# 20250520零数组变换1
class Solution1:  # 超时
	def isZeroArray(self, nums, queries):
		for left, right in queries:
			for i in range(left, right + 1):
				if nums[i] > 0:
					nums[i] -= 1
		return all(x == 0 for x in nums)
## 灵神题解——差分数组
class Solution2:
	def isZeroArray(self, nums, queries):
		diff = [0] * (len(nums) + 1)
		for left, right in queries:
			diff[left] -= 1
			diff[right + 1] += 1

		new_arr = list(accumulate(d))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, new_arr))
	
if __name__ == '__main__':
	nums = [4,3,2,1]
	queries = [[1,3],[0,2]]
	print(Solution1().isZeroArray(nums, queries))