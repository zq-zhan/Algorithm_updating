from math import inf

class Solution:
	def findKDistantIndices(self, nums, key, k):
		ans = set()
		n = len(nums)
		for i in range(n):
			if nums[i] == key:
				start = max(0, i - k)
				end = min(i + k, n - 1)
				for j in range(start, end + 1):
					ans.add(j)
				if end >= n:
					break
		return list(ans)
## 灵神题解
class Solution:
	def findKDistantIndices(self, nums, key, k):
		last = -inf
		for i in range(k - 1, -1, -1):
			if nums[i] == key:
				last = i
				break

		ans = []
		n = len(nums)
		for i in range(n):
			if i + k < n and nums[i + k] == key:
				last = i + k
			if last >= i - k:
				ans.append(i)
		return ans
	
if __name__ == '__main__':
	nums = [3,4,9,1,3,9,5]
	key = 9
	k = 1
	print(Solution().findKDistantIndices(nums, key, k))