class Solution:
	def successfulPairs(self, spells, potions, success):
		potions.sort()
		ans = [0] * len(spells)
		spells = [(x, i) for i, x in enumerate(spells)]
		spells.sort(reverse = True)
		j = 0
		m = len(potions)
		for x, i in spells:
			while j < m and potions[j] * x < success:
				j += 1
			ans[i] = m - j
		return ans
	
if __name__ == '__main__':
	spells = [5, 1, 3]
	potions = [1,2,3,4,5]
	success = 7
	print(Solution().successfulPairs(spells, potions, success))