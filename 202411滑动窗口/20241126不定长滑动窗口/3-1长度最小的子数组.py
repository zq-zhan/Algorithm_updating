# 灵神滑动窗口:while循环结束后更新答案
class Solution2:
	def minSubArrayLen(self,target,nums):
		n=len(nums)
		ans=n+1
		s=left=0
		for right,x in enumerate(nums): # 枚举子数组右端点
			s += x
			while s-nums[left] >= target:  #尽量缩短子数组长度
				s -= nums[left]
				left += 1
			if s >= target:
				ans=min(ans,right-left+1)
		return ans if ans<=n else 0
## 灵神滑动窗口：while循环内更新答案
class Solution2:
	def minSubArrayLen(self,target,nums):
		n=len(nums)
		ans=n+1
		s=left=0
		for right,x in enumerate(nums):
			s+=x
			while s>=target:
				ans=min(ans,right-left+1)
				s-=nums[left]
				left += 1
		return ans if ans<n else 0
			
# 1.长度最小的子数组
class Solution5:
	def minSubArrayLen(self, target, nums):
		ans = len(nums) + 1
		left = 0
		sum_win = 0
		for right, c in enumerate(nums):
			sum_win += c
			while sum_win >= target:
				ans = min(ans, right - left + 1)
				sum_win -= nums[left]
				left += 1
		return ans if ans <= len(nums) else 0
	
class Solution1:
	def minSubArrayLen(self, target, nums):
		if sum(nums) < target:
			return 0

		ans = len(nums)
		left = 0
		temp_sum = 0
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans

if __name__ == '__main__':
	nums=[2,3,1,2,4,3]
	target=7
	s=Solution5()
	print(s.minSubArrayLen(target,nums))