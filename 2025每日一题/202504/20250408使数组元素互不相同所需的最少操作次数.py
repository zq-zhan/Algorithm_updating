from collections import defaultdict

# 20250408使数组元素互不相同所需的最少操作次数
class Solution1:
	def minimumOperations(self, nums):
		dic_win = defaultdict(int)
		n = len(nums)
		for i in range(n - 1, -1, -1):
			dic_win[nums[i]] += 1
			if max(dic_win.values()) >= 2:
				return i // 3 + 1
		return 0
	
if __name__ == '__main__':
	nums = [1,2,3,4,2,3,3,5,7]
	print(Solution1().minimumOperations(nums))