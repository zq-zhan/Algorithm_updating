# 最高频元素的频数
class Solution1():
	def maxFrequency(self,nums,k):
		# nums.sort()
		nums=sorted(nums)
		ans=left=0
		total=0
		for right,c in enumerate(nums):
			total+=c
			while c*(right-left+1)>total+k:
				total-=nums[left]
				left +=1
			ans=max(ans,right-left+1)
		return ans
	
if __name__ == '__main__':
	nums=[1,1,1,2,2,3]
	k=2
	s=Solution1()
	print(s.maxFrequency(nums,k))