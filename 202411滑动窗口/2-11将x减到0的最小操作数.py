# 将x减到0的最小操作数
## 方法一：逆向思维
class Solution1():
	def minOperations(self,nums,k):
		ans=-1
		left=0
		total_win=0
		total=sum(nums)
		target_num=total-k
		if target_num<0:
			return -1
		for right,c in enumerate(nums):
			total_win+=c
			while total_win>target_num:
				total_win -= nums[left]
				left += 1
			if total_win==target_num:
				# cnt+=1
				ans=max(ans,right-left+1)
		if ans!=-1:
			return len(nums)-ans
		else:
			return -1

if __name__=="__main__":
	nums=[1,1]
	k=3
	s=Solution1()
	print(s.minOperations(nums,k))