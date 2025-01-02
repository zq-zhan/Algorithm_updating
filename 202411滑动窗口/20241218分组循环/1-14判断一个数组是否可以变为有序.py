# 14. 判断一个数组是否可以变为有序
class Solution1:
	def canSortArray(self,nums):
		i = 0
		n = len(nums)
		temp_num = 0
		while i < n:
			start = i
			i += 1
			cnt = bin(nums[start])[2:].count('1')
			while i < n and bin(nums[i])[2:].count('1') == cnt:
				i += 1
			if temp_num <= min(nums[start:i]):
				temp_num = max(nums[start:i])
			else:
				return False
		return True
# 灵神思路
class Solution2:
	def canSortArray(self,nums):
		n = len(nums)
		i = pre_max = 0
		while i < n:
			mx = 0
			start = i 
			i += 1
			ones_cnt = nums[start].bit_count()
			while i < n and nums[i].bit_count() == ones_cnt:
				if nums[i] < pre_max:
					return False
				mx = max(mx, nums[i])
				i += 1
			pre_max = mx
		return True
	
if __name__ == '__main__':
	nums = [3,16,8,4,2]
	cls = Solution1()
	print(cls.canSortArray(nums))