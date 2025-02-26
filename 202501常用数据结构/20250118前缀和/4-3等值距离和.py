# 3.等值距离和
from collections import defaultdict
from itertools import accumulate

## 灵神题解：按照相同元素分组后再计算
class Solution1:
	def distance(f, nums):
		groups = defaultdict(list)
		for i, x in enumerate(nums):
			groups[x].append(i)  # 相同元素分到同一组
		ans = [0] * len(nums)
		for a in groups.values():
			n = len(a)
			s = list(accumulate(a, initial = 0))
			for j, target in enumerate(a):
				left = target * j - s[j]  # left = q * j - s[j]
				right = s[n] - s[j] - target * (n - j)  # right = s[n] - s[j] - q * (n - j)
				ans[target] = left + right
		return ans
	
if __name__ == '__main__':
	nums = [1,3,1,1,2]
	cls = Solution1()
	print(cls.distance(nums))