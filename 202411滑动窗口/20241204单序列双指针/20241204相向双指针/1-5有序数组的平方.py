# 5.有序数组的平方
class Solution1:
	def sortedSquares(self,nums):
		ans_lis=[]
		for i in range(len(nums)):
			ans_lis.append(nums[i]**2)
		return sorted(ans_lis)
	
## 灵神
### 思路一：
class Solution2:
	def sortedSquares(self,nums):
		n=len(nums)
		ans_lis=[0]*n
		left,right=0,n-1
		for i in range(n-1,-1,-1):
			x=nums[left]*nums[left]
			y=nums[right]*nums[right]
			if x>y:
				ans_lis[i]=x
				left+=1
			else:
				ans_lis[i]=y
				right-=1
		return ans_lis
### 思路二：每次只需判断-nums[i]>nums[j]是否成立
class Solution3:
	def sortedSquares(self,nums):
		n=len(nums)
		ans=[0]*n
		left,right=0,n-1
		for i in range(n-1,-1,-1):
			x,y=nums[left],nums[right]
			if -x>y:
				ans[i]=x*x  # x*x比x**2快
				left+=1
			else:
				ans[i]=y*y
				right-=1
		return ans
	
class Solution:
	def sortedSquares(self,nums):
		ans=[]
		left,right=0,len(nums)-1
		while left<=right:  
			a=nums[left]*nums[left]  # 边界最大
			b=nums[right]*nums[right]
			if a<b:
				ans.append(b)  # 先进入最大的元素
				right-=1
			else:
				ans.append(a)
				left+=1
		return ans[::-1]


if __name__ == '__main__':
	nums = [-4,-1,0,3,10]
	cls=Solution()
	print(cls.sortedSquares(nums))