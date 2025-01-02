# 7.咒语和药水的成功对数
from bisect import bisect_left


class Solution1:
	def successfulPairs(self,spells,potions,success):
		ans = []
		potions.sort()
		for x in spells:
			find = bisect_left(potions, success/x)
			if find == len(potions):
				ans.append(0)
			else:
				ans.append(len(potions) - find)
		return ans
	
class Solution2:
	def successfulPairs(self, spells, potions, success):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		ans = []
		potions.sort()
		for x in spells:
			find = lower_bound(potions, success/x)
			ans.append(len(potions) - find)
		return ans

	
if __name__ == '__main__':
	spells = [5,1,3]
	potions = [1,2,3,4,5]
	success = 7
	s = Solution2()
	print(s.successfulPairs(spells,potions,success))