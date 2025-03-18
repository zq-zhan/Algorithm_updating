from collections import defaultdict

class Solution1:
	def largestInteger(self, nums, k):
		temp_win = defaultdict(int)
		for x in nums:
			temp_win[x] += 1
		only_num_lis = []
		for x in temp_win:
			if temp_win[x] == 1:
				only_num_lis.append(x)
		if not only_num_lis:
			return -1
		if k == 1 or k == len(nums) :
			return max(only_num_lis)
		else:
			a = nums[0]
			b = nums[-1]
			if a in only_num_lis and b in only_num_lis:
				return max(a, b)
			elif a in only_num_lis and b not in only_num_lis:
				return a
			elif a not in only_num_lis and b in only_num_lis:
				return b
			else:
				return -1

class Solution2:
	def largestInteger(self, nums, k):
		n = len(nums)	
		if k == n:
			return max(nums)
		temp_win = defaultdict(int)
		for i in range(n - k + 1):
			for j in range(i, i + k):
				temp_win[nums[j]] += 1
		ans = -1
		for x in temp_win:
			if temp_win[x] == 1:
				ans = max(ans, x)
		return ans


if __name__ == '__main__':
	nums = [0,0]
	k = 1
	print(Solution2().largestInteger(nums, k))