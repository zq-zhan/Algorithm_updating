# 2.统计公平数对的数目
class Solution1:
	def countFairPairs(self,nums,lower,upper):
		nums.sort()
		n = len(nums)
		p1 = 0
		p2 = n - 1
		ans = 0
		while p2 > 0:
			while p1 < p2:
				if nums[p1] + nums[p2] > upper:
					p1 = 0
					p2 -= 1
					break 
				elif nums[p1] + nums[p2] >= lower and nums[p1] + nums[p2] <= upper:
					p1 += 1
					ans += 1
				elif nums[p1] + nums[p2] < lower:
					p1 += 1
			if p1 == p2:
				p2 -= 1
				p1 = 0
		return ans

## 灵神思路:三指针
class Solution2:
	def countFairPairs(self,nums,lower,upper):
		ans = 0
		nums.sort()
		left = right = len(nums)
		for j,x in enumerate(nums):
			while right and nums[right - 1] > upper - x:
				right -= 1
			while left and nums[left - 1] >= lower - x:
				left -= 1
			ans += min(right, j) - min(left, j)
		return ans

if __name__ == '__main__':
	nums = [1,7,9,2,5]
	lower = 11
	upper = 11
	s = Solution2()
	print(s.countFairPairs(nums,lower,upper))