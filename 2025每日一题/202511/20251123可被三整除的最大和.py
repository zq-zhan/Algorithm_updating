from collections import Counter
from functools import cache
from math import inf

class Solution:
	def maxSumDivThree(self, nums):
		nums_dic = Counter(nums)
		temp_s = 0
		temp_mod_1 = []
		temp_mod_2 = []
		for key, value in nums_dic.items():
			if key % 3 == 0:
				temp_s += key * value
			elif key % 3 == 1:
				temp_mod_1.extend([key] * value)
			else:
				temp_mod_2.extend([key] * value)
		temp_mod_1.sort(reverse = True)
		temp_mod_2.sort(reverse = True)
		n, m = len(temp_mod_1), len(temp_mod_2)
		if n > m:
			temp_mod_2.extend([0] * (n - m))
		else:
			temp_mod_1.extend([0] * (m - n))
		i = j = 0
		n = max(n, m)
		while i < n and j < m:
			if i < n - 2 and sum(temp_mod_1[i:i + 3]) > temp_mod_1[i] + temp_mod_2[j]:
				temp_s += sum(temp_mod_1[i:i + 3])
				i += 3
			elif j < m - 2 and sum(temp_mod_2[j:j + 3]) > temp_mod_1[i] + temp_mod_2[j]:
				temp_s += sum(temp_mod_2[j:j + 3])
				j += 3
			else:
				temp_s += temp_mod_1[i] + temp_mod_2[j]
				i += 1
				j += 1
		return temp_s

## 动态规划
class Solution:
	def maxSumDivThree(self, nums):
		@cache
		def dfs(i, j):
			if i < 0:
				return 0 if j == 0 else -inf
			return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])
		return dfs(len(nums) - 1, 0)
	
if __name__ == '__main__':
	nums = [3,6,5,1,8]
	print(Solution().maxSumDivThree(nums))