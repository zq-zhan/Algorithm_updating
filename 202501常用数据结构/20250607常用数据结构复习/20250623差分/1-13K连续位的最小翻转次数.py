# class Solution:
# 	def minKBitFlips(self, nums, k):
# 		n = len(nums)
# 		nums = nums + [0]
# 		new_arr = [0] * (n + 1)
# 		for i in range(n - k + 1):
# 			new_arr[i] += (1 - x)
# 			new_arr[i + k] -= (1 - x)

# 		pre_s = list(accumulate(new_arr))[:-1]
## 
class Solution:
	def minKBitFlips(self, nums, k):
		n = len(nums)
		diff = [0] * (n + 1)
		ans, revCnt = 0, 0
		for i in range(n):
			revCnt += diff[i]
			if (nums[i] + revCnt) % 2 == 0:
				if i + k > n:
					return -1
				ans += 1
				revCnt += 1
				diff[i + k] -= 1
		return ans
	
if __name__ == '__main__':
	nums = [0, 1, 0]
	k = 1
	print(Solution().minKBitFlips(nums, k))