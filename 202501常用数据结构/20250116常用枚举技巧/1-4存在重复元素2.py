from collections import defaultdict

class Solution1:
	def containsNearbyDuplicate(self, nums, k):
		idx = defaultdict(list)
		for j, x in enumerate(nums):
			if x in idx:
				if abs(j - idx[x][-1]) <= k:
					return True
				# for c in idx[x]:
				# 	if abs(c - j) <= k:
				# 		return True
			idx[x].append(j)
		return False

## 灵神题解
class Solution2:
	def containsNearbyDuplicate(self, nums, k):
		last = {}
		for j, x in enumerate(nums):
			if x in last and j - last[x] <= k:
				return True
			last[x] = j  # 记录每个数x上一次出现的位置的下标
		return False
	
if __name__ == '__main__':
	nums = [1,2,3,1]
	k = 3
	cls = Solution2()
	print(cls.containsNearbyDuplicate(nums, k))