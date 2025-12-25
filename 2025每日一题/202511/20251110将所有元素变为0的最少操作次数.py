class Solution:
	def minOperations(self, nums):
		ans = 1
		new_arr = list(set(nums))
		new_arr.sort()
		n = len(nums)
		for x in new_arr[1:]:
			for i in range(1, n):
				if nums[i] >= x:
					continue
				ans += 1
			ans += 1
		return ans

## 灵神题解
class Solution:
	def minOperations(self, nums):
		ans = 0
		st = []
		for x in nums:
			while st and x < st[-1]:
				st.pop()
				ans += 1
			if not st or x != st[-1]:
				st.append(x)
		return ans + len(st) - (st[0] == 0)

## 暴力解法
class Solution:
	def minOperations(self, nums):
		ans = 0
		n = len(nums)
		for i in range(n):
			j = i + 1
			while j < n and nums[j] >= nums[i]:
				j += 1
			ans += 1
		return ans


if __name__ == '__main__':
	nums = [1,2,3,2,1]
	print(Solution().minOperations(nums))