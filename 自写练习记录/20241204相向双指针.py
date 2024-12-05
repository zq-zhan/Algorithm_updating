# 2.验证回文串
class Solution:
	def isPalindrome(self,s):
		left,right=0,len(s)-1
		while left<right:
			while left<right and not s[left].isalnum():  # 判断字符串是否是字母或数字
				left+=1
			while left<right and not s[right].isalnum():
				right-=1
			if s[left].lower() != s[right].lower():
				return False
			left+=1
			right-=1
		return True


# 删除字符串两端相同字符后的最短长度
class Solution1:
	def minimumLength(self,s):
		n=len(s)
		# ans=n
		left,right=0,n-1
		# target_char=s[0]
		while left<right and s[left]==s[right]:
			while s[left]==s[left+1] and left+1<right:
				left+=1
			while s[right]==s[right-1] and right-1>left:
				right-=1
			left+=1
			right-=1
		return right-left+1
## 思路二：
class Solution2:
	def minimumLength(self,s):
		n=len(s)
		left,right=0,len(s)-1
		while left<right and s[left]==s[right]:
			c=s[left]
			while left<=right and s[left]==c:
				left+=1
			while right>=left and s[right]==c:
				right-=1
		return right-left+1

# 4.给植物浇水
class Solution1:
	def minimumRefill(self,plants,capacityA,capacityB):
		left,right=0,len(plants)-1
		cnt=0
		origin_A=capacityA
		origin_B=capacityB
		while left<=right:
			if left<right:
				if capacityA<plants[left]:
					cnt+=1
					capacityA=origin_A
				if capacityB<plants[right]:
					cnt+=1
					capacityB=origin_B
			else:
				if max(capacityA,capacityB)<plants[left]:
					cnt+=1
			capacityA-=plants[left]
			capacityB-=plants[right]
			left+=1
			right-=1
		return cnt
## 思路二：优化
class Solution1:
	def minimumRefill(self,plants,capacityA,capacityB):
		left,right=0,len(plants)-1
		cnt=0
		origin_A=capacityA
		origin_B=capacityB
		while left<right:
			if capacityA<plants[left]:
				cnt+=1
				capacityA=origin_A
			if capacityB<plants[right]:
				cnt+=1
				capacityB=origin_B
			capacityA-=plants[left]
			capacityB-=plants[right]
			left+=1
			right-=1
		if left==right and max(capacityA,capacityB)<plants[left]:
			cnt+=1
		return cnt

# 5.有序数组的平方
## 思路一：O(n2)
class Solution1:
	def sortedSquares(self,nums):
		for i in range(len(nums)):
			nums[i]=nums[i]**2
		return sorted(nums)
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
			a=nums[left]*nums[left]
			b=nums[right]*nums[right]
			if a<b:
				ans.append(b)
				right-=1
			else:
				ans.append(a)
				left+=1
		return ans[::-1]

# 6.找到k个最接近的元素
class Solution1:
	def findClosestElements(self,arr,k,x):
		n=len(arr)
		left,right=0,n-1
		# ans=[0]*n
		for i in range(n-1,-1,-1):
			left_x=abs(arr[left]-x)
			right_y=abs(arr[right]-x)
			if left_x<right_y or (left_x==right_y and arr[left]<arr[right]):
				ans[i]=arr[right]
				right-=1
			else:
				ans[i]=arr[left]
				left+=1
		return ans
## 灵神思路
class Solution2:
	def findClosestElements(self,arr,k,x):
		left,right=0,len(arr)-1
		ans=[]
		while left<right and right-left+1>k:
			if abs(arr[left]-x)<=abs(arr[right]-x):
				right-=1
			else:
				left+=1
		return ans[left:right+1]
