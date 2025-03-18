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
			ans=max(ans,right-left+1)  # 错解
		return ans
	

class Solution2:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = 0 
		left = 0
		for right, c in enumerate(nums):
			cnt_win += 1 if c == 0 else 0
			while cnt_win > 1:
				cnt_win -= 1 if nums[left] == 0 else 0
				left += 1
			ans = max(ans, right - left)
		return ans
	
if __name__=='__main__':
	nums=[1,1,0,1]
	cls=Solution2()
	print(cls.longestSubarray(nums))