from collections import Counter

class Solution:
	def minOperations(self, nums):
		ans = left = 0
		nums_dic = Counter(nums)

		repeat_count = 0
		for count in nums_dic.values():
			if count > 1:
				repeat_count += 1

		for right, x in enumerate(nums):
			if left == right and repeat_count == 0:
				return ans

			if nums_dic[x] == 2:
				repeat_count -= 1
			nums_dic[x] -= 1
			if nums_dic[x] == 0:
				del nums_dic[x]
			ans = right // 3 + 1
			if right - left + 1 < 3:
				continue
			left = right + 1
		return ans
			
if __name__ == '__main__':
	nums = [4,3,5,1,2]
	print(Solution().minOperations(nums))