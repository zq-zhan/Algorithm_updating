# 11.采购方案
class Solution1:
	def purchasePlans(self,nums,target):
		nums.sort()
		left,right=0,len(nums)-1
		cnt=0
		while left<right:
			if nums[left]+nums[right]<=target:
				cnt+=right-left
				left+=1
			else:
				right-=1
		return cnt%1000000007