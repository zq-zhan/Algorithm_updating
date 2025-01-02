# 1. 统计移除递增子数组的数目
class Solution1:
	def incremovableSubarrayCount(self,nums):
		n=len(nums)
		i=0
		while i<n-1 and a[i]<a[i+1]:
			i+=1
		if i==n-1:  # 每个非空子数组都可以删除
			return n*(n+1)//2

		ans=i+2
		j=n-1
		while j==n-1 or a[j]<a[j+1]:
			while i>=0 and a[i]>=a[j]:
				i-=1
			ans+=i+2
			j-=1
		return ans