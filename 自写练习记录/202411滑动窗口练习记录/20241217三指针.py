# 1.等差三元组的数目
class Solution1:
	def arithmeticTriplets(self,nums,diff):
		p1 = 0
		ans = 0
		while p1 < n - 2:
			p2 = p1 + 1
			p3 = p2 + 1
			while p2 < n -1 and p3 < n:
				if nums[p3] - nums[p2] < diff:
					p3 += 1
				if nums[p2] - nums[p1] < diff:
					p2 += 1
					p3 += 1
				if nums[p2] - nums[p1] == nums[p3] - nums[p2] == diff:
					ans += 1
					p2 += 1
					p3 += 1
		return ans
# 灵神思路
class Solution2:
	def arithmeticTriplets(self,nums,diff):
		ans, i, j = 0, 0, 1
		for x in nums:  # 枚举第三个数
			while nums[j] + diff < x:
				j += 1
			if nums[j] + diff > x:
				continue
			while nums[i] + diff * 2 < x:
				i += 1
			if nums[i] + diff * 2 == x:
				ans += 1
		return ans

class Solution3:
	def arithmeticTriplets(self,nums,diff):
		ans, i, j, k = 0, 0, 1, 2
		n = len(nums)
		while k < n:  # 枚举第三个数
			while nums[j] + diff < nums[k]:
				j += 1
			if nums[j] + diff > nums[k]:
				k += 1
				continue
			while nums[i] + diff * 2 < nums[k]:
				i += 1
			if nums[i] + diff * 2 == nums[k]:
				ans += 1
				k += 1
		return ans

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
'''调试了一下，这里三指针的思路是枚举nums[j]，找到一个[left+1:right+1]窗口内的元素nums[i]
均符合nums[i]+nums[j]满足题意的元素，元素个数为right-left。
但是枚举的时候，不一定能保证这个窗口内i的序号就是小于j的，所以要取min。 
两次while分别是找到能满足nums[i]+nums[j]<=upper的最大的right，
和刚好不满足nums[i]+nums[j]>=lower的最大left（实际满足的为left+1），
所以元素个数为right-(left+1)+1=right-left。'''
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

# 3.区间子数组个数
class Solution1:
	def numSubarrayBoundedMax(self,nums,left,right):
		