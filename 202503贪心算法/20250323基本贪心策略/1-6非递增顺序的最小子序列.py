# 6.非递增顺序的最小子序列
class Solution1:
	def minSubsequence(self, nums):
		nums.sort(reverse = True)
		s = sum(nums)
		ans = []
		for x in nums:
			ans.append(x)
			if sum(ans) > s - sum(ans):
				break
		return ans
	
if __name__ == '__main__':
	nums = [4,3,10,9,8]
	print(Solution1().minSubsequence(nums))