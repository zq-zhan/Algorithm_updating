
# 6.对数组执行操作
class Solution1:
	def applyOperations(self,nums):
		fast=0
		while fast<len(nums)-1:
			if nums[fast]==nums[fast+1]:
				nums[fast]=nums[fast]*2
				nums[fast+1]=0
				fast+=1
			fast+=1
		left,right=0,len(nums)-1
		while left<right and nums[left]==0:
			temp=nums[left]
			nums[left]=nums[right]
			nums[right]=temp
			left+=1
			right-=1
		return nums

class Solution2:
	def applyOperations(self,nums):
		fast=0
		while fast<len(nums)-1:
			if nums[fast]==nums[fast+1]:
				nums[fast]=nums[fast]*2
				nums[fast+1]=0
				fast+=1
			fast+=1
		k=0
		for i in range(len(nums)):
			if nums[i]!=0:
				temp=nums[i]
				nums[i]=0
				nums[k]=temp
				k+=1
		return nums

if __name__ == '__main__':
	nums=[1,2,2,1,1,0]
	s=Solution2()
	print(s.applyOperations(nums))