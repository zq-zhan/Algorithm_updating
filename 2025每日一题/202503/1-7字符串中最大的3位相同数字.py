# 7.字符串中最大的3位相同数字
from string import digits


class Solution1:
	def largestGoodInteger(self, nums):
		ans = ''
		temp_mx = 0
		for i in range(2, len(nums)):
			if nums[i] == nums[i - 1] == nums[i - 2]:
				if nums[i] >= temp_mx:
					temp_mx = nums[i]
					ans = str(nums[i]) * 3
		return ans
## 灵神优化
class Solution2:
	def largestGoodInteger(self, nums):
		mx = ''
		cnt = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				cnt = 1
				continue
			cnt += 1
			if cnt == 3 and nums[i] > mx:
				mx = nums[i]
		return mx * 3
	
class Solution3:
	def largestGoodInteger(self, nums):
		ans = ''
		for i in range(2, len(nums)):
			if nums[i] == nums[i - 1] == nums[i - 2]:
				if nums[i] > ans:
					ans = nums[i]
		return ans * 3

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in reversed(digits):  # 倒序遍历数字，取最大的3位相同数字
            s = d * 3
            if s in num:
                return s
        return ""

if __name__ == '__main__':
	num = '6777133339'
	cls = Solution()
	print(cls.largestGoodInteger(num))