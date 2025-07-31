class Solution:
	def smallestSubarrays(self, nums):
		n = len(nums)
		sub_or = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			sub_or[i] = sub_or[i + 1] | nums[i]

		ans = []
		for i, x in enumerate(nums):
			for j in range(i, n):
				x |= nums[j]
				if x == sub_or[i]:
					ans.append(j - i + 1)
					break
		return ans
	
if __name__ == '__main__':
	nums = [1,0,2,1,3]
	print(Solution().smallestSubarrays(nums))