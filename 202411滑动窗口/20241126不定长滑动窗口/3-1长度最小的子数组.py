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
			

if __name__ == '__main__':
	nums=[2,3,1,2,4,3]
	target=7
	s=Solution2()
	print(s.minSubArrayLen(target,nums))