# 9.最长奇偶子数组
class Solution1:
	def longestAlternatingSubarray(self,nums,threshold):
		ans = 0
		left, right = 0, 1
		while right < len(nums):
			while nums[left] <= threshold and nums[left] % 2 != 0:
				left += 1
				# right += 1
			if right < len(nums) and (nums[right]> threshold or nums[right] % 2 == nums[right - 1] % 2):
				if nums[left] % 2 == 0 and nums[left] <= threshold:
					ans = max(ans, right - left)
				left = right
			right += 1
		if nums[left] % 2 == 0 and nums[left] <= threshold:
			ans = max(ans, right - left)
		return ans
	
## 灵神思路：不易错！！！
class Solution2:
	def longestAlternatingSubarray(self,nums,threshold):
		ans = i = 0
		while i < len(nums):
			if nums[i] > threshold or nums[i] % 2 != 0:
				i += 1
				continue
			start = i
			i += 1
			while i < len(nums) and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
				i += 1
			ans = max(ans, i - start)
		return ans
	
if __name__ == '__main__':
	nums = [3,2,5,4]
	threshold = 5
	s = Solution2()
	print(s.longestAlternatingSubarray(nums,threshold))