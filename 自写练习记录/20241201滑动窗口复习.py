# 定长滑动窗口
## 定长子串中元音的最大数目
### 错误点：if判断条件错误
class Solution:
	def maxVowels(self,s,k):
		ans=cnt=0
		for i,c in enumerate(s):
			cnt+=1 if c in "aeiou" else 0
			if i <= k-1:
				continue
			ans=max(ans,cnt)
			cnt-=1 if s[i-k+1] in "aeiou" else 0
		return ans
## 子数组最大平均数
### 错误点：ans初始化错误
class Solution:
	def findMaxAverage(self,nums,k):
		ans=float('-inf')
		total=0
		for i,c in enumerate(nums):
			total+=c 
			if i<k-1:
				continue
			ans=max(ans,total)
			total-=nums[i-k+1]
		return ans/k
## 大小为K且平均值大于等于阈值的子数组数目
class Solution:
	def numOfSubarrays(self,arr,k,threshold):
		ans=0
		total=0
		for i,c in enumerate(arr):
			total+=c
			if i<k-1:
				continue
			if total/k>=threshold:
				ans+=1
			total-=arr[i-k+1]
		return ans