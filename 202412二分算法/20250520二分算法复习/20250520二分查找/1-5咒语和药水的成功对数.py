class Solution1:
	def successfulPairs(self, spells, potions, success):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		potions.sort()
		ans = []
		n = len(potions)
		for spell in spells:
			ans.append(n - lower_bound(potions, success / spell))
		return ans
	
if __name__ == '__main__':
	spells = [5,1,3]
	potions = [1,2,3,4,5]
	success = 7
	print(Solution1().successfulPairs(spells, potions, success))