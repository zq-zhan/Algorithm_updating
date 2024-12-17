# 最大连续1的个数
class Solution1():
	def longestOnes(self,nums,k):
		ans=left=0
		cnt_0=0
		for right,c in enumerate(nums):
			cnt_0 += 1 if c==0 else 0
			while cnt_0>k:
				cnt_0 -= 1 if nums[left]==0 else 0
				left += 1
			ans = max(ans,right-left+1)
		return ans