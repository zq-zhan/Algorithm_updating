# 2.和为K的子数组
from collections import defaultdict


class Solution1:
	def subarraySum(self, nums, k):
		def max_sum(target):
			temp_ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					temp_sum -= nums[left]
					left += 1
				temp_ans += left
			return temp_ans
		return max_sum(k) - max_sum(k + 1)
	
## 灵神题解
class Solution2:
	def subarraySum(self, nums, k):
		s = [0] * (len(nums) + 1)
		for i, x in enumerate(nums):
			s[i + 1] = s[i] + x

		ans = 0
		cnt = defaultdict(int)  # 记录前缀和出现的次数
		for sj in s:
			ans += cnt[sj - k]  # 统计在j左边（即出现在已遍历的前缀和中）使得s[j] - s[i] = k 即和为k的子数组个数
			cnt[sj] += 1  # 更新前缀和出现的次数
		return ans
	
## 灵神题解——方法二：一次遍历
class Solution3:
	def subarraySum(self, nums, k):
		ans = pre_sum = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		for i, c in enumerate(nums):
			pre_sum += c
			ans += cnt[pre_sum - k]
			cnt[pre_sum] += 1
		return ans


if __name__ == '__main__':
	nums = [-1, -1, 1]
	k = 1
	print(Solution3().subarraySum(nums, k))