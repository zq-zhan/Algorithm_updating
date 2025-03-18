from collections import defaultdict

class Solution1:
	def medianOfUniquenessArray(self, nums):
		ans_lis = []
		left = 0
		temp_win = defaultdict(int)
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max(temp_win.values()) > 1:
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
			ans_lis.extend(i + 1 for i in range(right - left + 1))
		ans_lis.sort()
		n = len(ans_lis)
		if n % 2 == 1:
			return ans_lis[n // 2]
		else:
			return min(ans_lis[n // 2], ans_lis[n // 2 - 1])
		
if __name__ == '__main__':
	nums = [3,4,3,4,5]
	print(Solution1().medianOfUniquenessArray(nums))