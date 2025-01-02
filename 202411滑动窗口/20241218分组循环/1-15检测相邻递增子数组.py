# 15.检测相邻递增子数组
class Solution1:
	def maxIncreasingSubarrays(self,nums):
		i = 0
		n = len(nums)
		ans = 1
		temp_lis = []
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] > nums[i - 1]:
				i += 1
			if i - start > 1:
				temp_lis.append([start,i-1])
			ans = max (ans, (i - start) // 2)
			if len(temp_lis) > 1 and start == temp_lis[-2][1] + 1:
				ans = max(ans, min(i - start, temp_lis[-2][1] - temp_lis[-2][0] + 1))
		return ans
	
class Solution2:
	def maxIncreasingSubarrays(self,nums):
		i = 0
		n = len(nums)
		ans = 1
		pre_len = 1
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] > nums[i - 1]:
				i += 1
			ans = max (ans, (i - start) // 2, min(pre_len, i - start))  # 可以直接min是因为不是相邻那么pre_len就会是1
			pre_len = i - start
		return ans
        
if __name__ == '__main__':
	nums = [-8,7,-16,-7,18]
	cls = Solution2()
	print(cls.maxIncreasingSubarrays(nums))