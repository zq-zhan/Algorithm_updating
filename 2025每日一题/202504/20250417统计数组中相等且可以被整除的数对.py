from collections import defaultdict

class Solution1:
	def countPairs(self, nums, k):
		ans = 0
		nums_dic = defaultdict(list)
		for i, c in enumerate(nums):
			nums_dic[c].append(i)

		for same_lis in nums_dic.values():
			if len(same_lis) < 2:
				continue
			# n = len(same_lis)
			# for i in range(n - 1):
			# 	ord_1 = same_lis[i]
			# 	for j in range(i + 1, n):
			# 		ord_2 = same_lis[j]
			# 		if (ord_1 * ord_2) % 2 == 0:
			# 			ans += 1 
			for i, x in enumerate(same_lis):
				for y in same_lis[i + 1:]:
					if (x * y) % k == 0:
						ans += 1
		return ans
	

## 优化
class Solution2:
	def countPairs(self, nums, k):
		ans = 0
		nums_dic = defaultdict(list)
		for j in range(len(nums)):
			val = nums[j]
			for i in nums_dic[val]:
				if (j * i) % k == 0:
					ans += 1
			nums_dic[val].append(j)
		return ans

if __name__ == '__main__':
	nums = [3,1,2,2,2,1,3]
	k = 2
	print(Solution2().countPairs(nums, k))