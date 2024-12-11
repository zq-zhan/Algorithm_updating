# 5.按奇偶排序数组
# 5.按奇偶排序数组
class Solution1:
	def sortArrayByParity(self,nums):
		left,right=0,len(nums)-1
		while left<right:
			if nums[left]%2==1 and nums[right]%2==0:
				temp=nums[left]
				nums[left]=nums[right]
				nums[right]=temp
				left+=1
				right-=1
			elif nums[left]%2==1 and nums[right]%2==1:
				right-=1
			elif nums[left]%2==0 and nums[right]%2==0:
				left+=1
			else:
				left+=1
				right-=1
		return nums
	
## 思路二
class Solution2:
	def sortArrayByParity(self,nums):
		slow,fast=0,0
		while fast<len(nums):
			if nums[fast]%2==0:  # 找到偶数和前面交换
				temp=nums[slow]
				nums[slow]=nums[fast]
				nums[fast]=temp
				slow+=1
			fast+=1
		return nums
	

if __name__ == '__main__':
	nums=[3,1,2,4]
	s=Solution2()
	print(s.sortArrayByParity(nums))