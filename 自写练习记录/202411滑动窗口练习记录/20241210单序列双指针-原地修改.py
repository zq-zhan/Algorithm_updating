# 1.移除元素
class Solution1:
	def removeElement(self,nums,val):
		slow=0
		for fast in range(len(nums)):
			if nums[fast]!=val:
				nums[slow]=nums[fast]
				slow+=1
		return slow

class Solution:
	def removeElement(self,nums,val):
		cnt=0
		for x in nums:
			if x!=val:
				nums[cnt]=x
				cnt+=1		
		return cnt



# 2.删除有序数组中的重复项
class Solution1:
	def removeDuplicates(self,nums):
		k=1
		for i in range(1,len(nums)):
			if nums[i]!=nums[i-1]:
				nums[k]=nums[i]
				k+=1
		return k
class Solution2:
	def removeDuplicates(self,nums):
		i=1
		cnt=1
		while i<len(nums):
			if nums[i]==nums[i-1]:
				nums[i]=nums[i+1]
			else:
				cnt+=1
			i+=1
		return cnt

# 3.删除有序数组中的重复项2
class Solution1:
	def removeDuplicates(self,nums):
		win_dic=Counter()
		cnt=-1
		for i in range(0,len(nums)):
			win_dic[nums[i]]+=1
			if win_dic[nums[i]]<=2:
				cnt+=1
				nums[cnt]=nums[i]
		return cnt
## 思路二：在有序条件下成立
class Solution2:
	def removeDuplicates(self,nums):
		k=2
		for i in range(2,len(nums)):
			if nums[i]!=nums[k-2]:
				nums[k]=nums[i]
				k+=1
		return k

# 4.移动零
class Solution1:
	def moveZeroes(self,nums):
		k=0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[k]=nums[i]
		nums[k:]=0
		return nums
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
			if nums[fast]%2==0:
				temp=nums[slow]
				nums[slow]=nums[fast]
				nums[fast]=temp
				slow+=1
			fast+=1
		return nums

# 5.按奇偶排序数组2
class Solution1:
	def sortArrayByParityII(self,nums):
		slow=0
		for fast in range(len(nums)):
			if (nums[fast]%2==0 and slow%2==0) or (nums[fast]%2==1 and slow%2==1):
				temp=nums[slow]
				nums[slow]=nums[fast]
				nums[fast]=temp
		return nums
## 不使用额外空间
class Solution2:
	def sortArrayByParityII(self,nums):
		slow=0
		for fast in range(1,len(nums),2):
			while nums[fast]%2==0:
				temp=nums[fast]
				nums[fast]=nums[slow]
				nnums[slow]=temp
				slow+=2
		return nums

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
		slow=len(nums)-1
		for fast2 in range(len(nums)):
			if nums[fast2]==0:
				temp=nums[slow]
				nums[slow]=0
				nums[fast2]=temp
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

# 7.复写零
class Solution1:
	def duplicateZeros(self,arr):
		i=0
		while i < len(arr):
			if nums[i]==0:
				for j in range(len(arr)-1,i+1):
					nums[j]=nums[j-1]
				nums[i+1]=0
				i+=1
			i+=1
		return nums
## 思路二：O(n)
class Solution2:
	def duplicateZeros(self,arr):
		n=len(arr)
		zeros_num=sum(1 for x in arr if x==0)
		j=n+zeros-1

		for i in range(n-1,-1,-1):
			if j<n:
				arr[j]=arr[i]
			j-=1
			if arr[i]==0:
				if j<n:
					arr[j]=0
				j-=1
		return arr[:n]	
## 思路三：栈
class Solution3:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        idx, cnt = 0, 0
        while cnt < n:
            if arr[idx] == 0:
                cnt += 1
            idx += 1
            cnt += 1
        i, j = n - 1, idx - 1
        if arr[j] == 0 and cnt > n:
            arr[i] = 0
            i -= 1
            j -= 1
        while i > 0:
            arr[i] = arr[j]
            i -= 1
            if arr[j] == 0:
                arr[i] = 0
                i -= 1
            j -= 1
        return arr


