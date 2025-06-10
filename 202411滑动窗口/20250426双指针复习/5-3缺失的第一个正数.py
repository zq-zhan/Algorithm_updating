class Solution1:
	def firstMissingPositive(self, nums):
		max_num = max(nums)
		if max_num <= 0:
			return 1
		if len(nums) == 1:
			if nums[0] > 1 or nums[0] <= 0:
				return 1
			else:
				return 2
		temp_lis = [0] * max_num
		for x in nums:
			if x <= 0:
				continue
			temp_lis[x - 1] = 1

		for i, c in enumerate(temp_lis):
			if c != 1:
				return i + 1
		return max_num + 1
	
class Solution1:
	def firstMissingPositive(self, nums):
		nums = set(nums)
		for i in range(2 ** 31 - 1):
			if i + 1 not in nums:
				return i + 1
			
## 灵神题解
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # 如果当前学生的学号在 [1,n] 中，但（真身）没有坐在正确的座位上
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 那么就交换 nums[i] 和 nums[j]，其中 j 是 i 的学号
                j = nums[i] - 1  # 减一是因为数组下标从 0 开始
                nums[i], nums[j] = nums[j], nums[i]

        # 找第一个学号与座位编号不匹配的学生
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 所有学生都坐在正确的座位上
        return n + 1
			
if __name__ == '__main__':
	nums = [1,1,2]
	print(Solution().firstMissingPositive(nums))