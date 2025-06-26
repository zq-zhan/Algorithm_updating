# 4.数组中重复的数据
# class Solution1:  # 空间复杂度O(n)不符合要求
# 	def findDuplicates(self, nums):
# 		ans = []
# 		dic_win = defaultdict(int)
# 		for x in nums:
# 			if dic_win[x] == 1:
# 				ans.append(x)
# 			dic_win[x] += 1
# 		return ans
## 优化
class Solution1:
	def findDuplicates(self, nums):
		ans = []
		n = len(nums)
		for x in nums:
			if nums[abs(x) - 1] < 0:
				ans.append(abs(x))
			else:
				nums[abs(x) - 1] = -nums[abs(x) - 1]
		return ans
	
if __name__ == '__main__':
	nums = [4,3,2,7,8,2,3,1]
	print(Solution1().findDuplicates(nums))