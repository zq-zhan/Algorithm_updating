# 8.汇总区间
class Solution1:
	def summaryRanges(self,nums):
		ans = []
		if len(nums) == 0:
			return ans
		left, right = 0, 1
		while right < len(nums):
			if nums[right] != nums[right - 1] + 1:
				if right - left > 1:
					ans.append(f"{nums[left]}->{nums[right - 1]}")
				else:
					ans.append(f"{nums[left]}")
				left = right
			right += 1
		if right - left > 1:
			ans.append(f"{nums[left]}->{nums[right - 1]}")
		else:
			ans.append(f"{nums[left]}")
		return ans
	
if __name__ == '__main__':
	nums = []
	cls = Solution1()
	print(cls.summaryRanges(nums))