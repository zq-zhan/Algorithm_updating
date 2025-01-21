# 2.好数对的数目
from collections import defaultdict

class Solution1:
	def numIdenticalPairs(self, nums):
		idx = defaultdict(list)
		ans = 0
		for j, x in enumerate(nums):
			if x in idx:
				ans += len(idx[x])
			idx[x].append(j)
		return ans
	
## 灵神题解
class Solution2:
	def numIdenticalPairs(self, nums):
		ans = 0
		cnt = defaultdict(int)
		for x in nums:
			ans += cnt[x]
			cnt[x] += 1
		return ans 
	
if __name__ == '__main__':
	nums = [1,2,3,1,1,3]
	s = Solution2()
	print(s.numIdenticalPairs(nums))