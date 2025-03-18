## 乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self,nums,k):
		ans=left=0
		plus_total=1
		if k<=1:
			return 0
		for right,c in enumerate(nums):
			plus_total*=c
			while plus_total>=k:
				plus_total/=nums[left]
				left+=1
			ans+=right-left+1
		return ans

class Solution2:
	def numSubarrayProductLessThanK(self, nums, k):
		ans = left = 0
		if k <= 1:
			return 0
		temp_plus = 1
		for right, c in enumerate(nums):
			temp_plus *= c
			while temp_plus >= k:
				temp_plus /= nums[left]
				left += 1
			ans += right - left + 1
		return ans

class Solution3:
	def numSubarrayProductLessThanK(self, nums, k):
		if k <= 1:
			return 0
		ans = left = 0
		plus_win = 1
		for right, c in enumerate(nums):
			plus_win *= c
			while plus_win >= k:
				plus_win /= nums[left]
				left += 1
			ans += right - left + 1
		return ans

if __name__ == '__main__':
	nums=[1,1,1]
	k=1
	s=Solution3()
	print(s.numSubarrayProductLessThanK(nums,k))