## 3.删掉一个元素以后全为1的最长子数组
class Solution_rv:
	def longestSubarray(self,nums):
		ans=left=0
		cnt_0=0
		for right,c in enumerate(nums):
			cnt_0+=(1-c)
			while cnt_0>1:
				cnt_0-=(1-nums[left])
				left+=1
			ans=max(ans,right-left+1)
		return ans
	
if __name__=='__main__':
	nums=[1,1,0,1]
	cls=Solution_rv()
	print(cls.longestSubarray(nums))