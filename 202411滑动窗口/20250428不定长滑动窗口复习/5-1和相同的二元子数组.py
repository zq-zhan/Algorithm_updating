## 分解为两个越长越合法问题
class Solution1:
	def numSubarraysWithSum(self, nums, goal):
		def over(target):
			temp_s = ans = left = 0
			for right, c in enumerate(nums):
				temp_s += c
				while left <= right and temp_s >= target:
					temp_s -= nums[left]
					left += 1
				ans += left
			return ans
		return over(goal) - over(goal + 1)
	

## 三指针做法
class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		temp_s1 = temp_s2 = ans = left1 = left2 = 0
		for right, c in enumerate(nums):
			temp_s1 += c
			temp_s2 += c
			while left1 <= right and temp_s1 >= goal:
				temp_s1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_s2 >= goal + 1:
				temp_s2 -= nums[left2]
				left2 += 1
			ans += left1 - left2
		return ans
	
if __name__ == '__main__':
	nums = [0,0,0,0,0]
	goal = 0
	print(Solution1().numSubarraysWithSum(nums, goal))