## 灵神题解——哈希表解法
class Solution2:
	def twoSum(Self, nums, target):
		idx = {}
		for j, x in enumerate(nums):  # 枚举右
			if target - x in idx:
				return [idx[target - x], j]
			idx[x] = j # 维护左
			
if __name__ == '__main__':
	nums = [3,2,4]
	target = 6
	print(Solution2().twoSum(nums, target)) # [0, 1]