# 19.长度为k的子数组的能量值2
class Solution1:
	def resultsArray(self,nums,k):
		i = 0
		n = len(nums)
		ans = [-1] * (n - k + 1)
		cnt = 0
		for i, x in enumerate(nums):
			if i == 0 or x == nums[i - 1] + 1:
				cnt += 1
			else:
				cnt = 1
			if cnt >= k:
				ans[i - k + 1] = x
		return ans

if __name__ == '__main__':
	nums = [1,2,3,4,3,2,5]
	k = 3
	cls = Solution1()
	print(cls.resultsArray(nums,k))
	