# 无限数组的最短子数组
from math import inf


class Solution1:
	def minSizeSubarray(self,nums,target):
		ans,left=inf,0
		total_win=0
		n=len(nums)
		win_len=0
		new_nums=nums+nums
		for right,c in enumerate(new_nums):
			total_win+=new_nums[right]
			win_len+=1
			while total_win>=target:
				if total_win==target:
					ans=min(ans,win_len)
				total_win-=new_nums[left]
				win_len-=1
				left+=1
		return ans
	
## 方法二：灵神不定长滑动窗口
class Solution2:
	def minSizeSubarray(self,nums,target):
		ans,left=inf,0
		total_win=0
		n=len(nums)
		win_len=0
		new_nums=nums+nums
		total=sum(nums)
		for right,c in enumerate(new_nums):
			total_win+=new_nums[right]
			win_len+=1
			while total_win>=target%total:
				if total_win==target%total:
					ans=min(ans,win_len)
					break
				total_win-=new_nums[left]
				win_len-=1
				left+=1
		return ans+target//total*n if ans!=inf else -1

class Solution3:
	def minSizeSubarray(self,nums,target):
		ans,left=inf,0
		total_win=0
		n=len(nums)
		win_len=0
		new_nums=nums+nums
		total=sum(nums)
		for right,c in enumerate(new_nums):
			total_win+=new_nums[right]
			win_len+=1
			while total_win>target%total:
				total_win-=new_nums[left]
				win_len-=1
				left+=1
			if total_win==target%total:
					ans=min(ans,win_len)
		return ans+target//total*n if ans!=inf else -1

## 灵神思路原版
class Solution:
    def minSizeSubarray(self, nums, target):
        total = sum(nums)
        n = len(nums)
        ans = inf
        left = s = 0
        for right in range(n * 2):
            s += nums[right % n]
            while s > target % total:
                s -= nums[left % n]
                left += 1
            if s == target % total:
                ans = min(ans, right - left + 1)
        return ans + target // total * n if ans < inf else -1


# class Solution1:
# 	def minSizeSubarray(self, nums, target):
# 		ans = inf
# 		left = 0
# 		temp_sum = 0
# 		n = len(nums)
# 		for right in range(0, 10 ** 5 + 1):
# 			temp_sum += nums[right % n]
# 			while temp_sum >= target:
# 				if temp_sum == target:
# 					ans = min(ans, right - left + 1)
# 				temp_sum -= nums[left % n]
# 				left += 1
# 		return ans if ans < inf else -1
	

## 关键：解析题意
## 灵神题解——
class Solution2:
	def minSizeSubarray(self, nums, target):
		total = sum(nums)
		n = len(nums)
		ans = inf
		left = s = 0
		for right in range(n * 2):
			s += nums[right % n]
			while s >= target % total:
				if s == target % total:
					ans = min(ans, right - left + 1)
				s -= nums[left % n]
				left += 1
		return ans + target // total * n if ans < inf else -1


if __name__=='__main__':
	nums=[1,1,1,2,3]
	target=10
	cls=Solution2()
	print(cls.minSizeSubarray(nums,target))