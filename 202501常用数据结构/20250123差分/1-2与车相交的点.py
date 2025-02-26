# 2.与车相交的点
from collections import Counter,defaultdict
from itertools import accumulate

# 2.与车相交的点
class Solution1:
	def numberOfPoints(self, nums):
		max_num = max(end for from_, end in nums)
		d = [0] * (max_num + 2)
		for from_, end in nums:
			d[from_] += 1
			d[end + 1] -= 1
		return sum(s > 0 for s in accumulate(d))
	
## 灵神题解
class Solution2:
	def numberOfPoints(self, nums):
		max_end = max(end for _, end in nums)
		diff = [0] * (max_end + 2)
		for start, end in nums:
			diff[start] += 1
			diff[end + 1] -= 1
		return sum(s > 0 for s in accumulate(diff))
	
## 方法二
class Solution3:
	def numberOfPoints(self, nums):
		d = defaultdict(int)
		for start, end in nums:
			d[start] += 1
			d[end + 1] -= 1
		ans = s = last = 0
		for cur, v in sorted(d.items()):  # d.items() 返回的是字典的键值对
			if s > 0:
				ans += cur - last
			s += v
			last = cur
		return ans

class Solution4:
	def numberOfPoints(self, nums):
		d = defaultdict(int)
		for start, end in nums:
			d[start] += 1
			d[end + 1] -= 1
		ans = temp_sum = last = 0
		for k in sorted(d):
			ans += k - last if temp_sum > 0 else 0
			temp_sum += d[k]
			last = k
		return ans

if __name__ == '__main__':
	nums = [[3,6],[1,5],[4,7]]
	cls = Solution4()
	print(cls.numberOfPoints(nums))