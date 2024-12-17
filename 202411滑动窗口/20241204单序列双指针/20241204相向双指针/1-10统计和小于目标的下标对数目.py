import time

# 10.统计和小于目标的下标对数目
# 复杂度：O(n)
class Solution1:
	def countPairs(self,nums,target):
		cnt=0
		left,right=0,len(nums)-1
		while left<right and left<len(nums)-1:
			if nums[left]+nums[right]<target:
				cnt+=1
			if right-left>1:
				right-=1
			else:
				left+=1
				right=len(nums)-1
		return cnt
## 灵神思路:O(nlogn)
class Solution2:
	def countPairs(self,nums,target):
		nums.sort()
		ans=left=0
		right=len(nums)-1
		while left<right:
			if nums[left]+nums[right]<target:
				ans+=right-left
				left+=1
			else:
				right-=1
		return ans
	
if __name__=='__main__':
	time1=time.time()
	nums=[-6,2,5,-2,-7,-1,3]
	target=-2
	s=Solution2()
	print(s.countPairs(nums,target))
	time2=time.time()
	print("执行耗时:"+str(time2-time1))