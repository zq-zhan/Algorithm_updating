# 4.移动零
class Solution1:
	def moveZeroes(self,nums):
		k=0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[k]=nums[i]
				k+=1
		nums[k:]=[0]*(len(nums)-k)
		return nums

## 思路二：
## 思路二：交换，实现不复制数组进行替换
class Solution2:
	def moveZeroes(self,nums):
		k=0
		for i in range(len(nums)):
			if nums[i]!=0:  #找到非零数与前面交换
				temp_i=nums[i]
				nums[i]=0
				nums[k]=temp_i
				k+=1
		return nums

if __name__ == '__main__':
	nums=[1]
	cls=Solution2()
	print(cls.moveZeroes(nums))