from collections import defaultdict

# 20250416统计好子数组的数目
class Solution1:
	def countGood(self, nums, k):
		dic_win = defaultdict(int)
		ans = 0
		left = 0
		right = 0
		n = len(nums)
		temp_ans = 0
		while right < n:
			dic_win[nums[right]] += 1
			temp_ans += dic_win[nums[right]] - 1
			# for val in dic_win.values():
			# 	temp_ans += val * (val - 1) // 2
			while temp_ans >= k:
				ans += n - right
				temp_ans -= dic_win[nums[left]] - 1
				dic_win[nums[left]] -= 1
				left += 1
			right += 1
		return ans
## 灵神写法
class Solution2:
	def countGood(self, nums, k):
		dic_win = defaultdict(int)
		ans, left, temp_ans = 0, 0, 0
		for x in nums:
			dic_win[x] += 1
			temp_ans += dic_win[x] - 1
			while temp_ans >= k:
				temp_ans -= dic_win[nums[left]] - 1
				dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans
	
if __name__ == '__main__':
	nums = [3,1,4,3,2,2,4]
	k = 2
	print(Solution1().countGood(nums, k))