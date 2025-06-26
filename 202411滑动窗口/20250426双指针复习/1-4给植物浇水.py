# 4.给植物浇水
class Solution1:
	def minimumRefill(self, plants, capacityA, capacityB):
		n = len(plants)
		ans = 0
		left, right = 0, n - 1
		curA = capacityA
		curB = capacityB
		while left <= right:
			if left < right:
				if plants[left] <= curA:
					curA -= plants[left]
				else:
					ans += 1
					curA = capacityA - plants[left]

				if plants[right] <= curB:
					curB -= plants[right]
				else:
					ans += 1
					curB = capacityB - plants[right]
			else:
				if max(curA, curB) < plants[left]:
					ans += 1
			left += 1
			right -= 1
		return ans
if __name__ == '__main__':
	plants = [2, 2, 3, 3]
	capacityA = 5
	capacityB = 5
	print(Solution1().minimumRefill(plants, capacityA, capacityB)) # Output: 1