class Solution1:
	def maxNumOfMarkedIndices(self, nums):
		def check(target):
			ans = 0
			p2 = n - 1
			p1 = p2 - 1
			while p1 >= 0 and p2 > 0:
				if 2 * nums[p1] <= nums[p2]:
					ans += 2
					p2 -= 1
					if ans >= target:
						return True
				p1 -= 1
			return False

		nums.sort()
		n = len(nums)
		left, right = 0, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left 
	
class Solution:
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		n = len(nums)
		ans = 0
		p2 = n - 1
		p1 = n // 2 - 1
		while p1 >= 0 and p2 > 0:
			if 2 * nums[p1] <= nums[p2]:
				ans += 2
				p2 -= 1
			p1 -= 1
		return ans

if __name__ == '__main__':
	# nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]
	nums = [57,40,57,51,90,51,68,100,24,39,11,85,2,22,67,29,74,82,10,96,14,35,25,76,26,54,29,44,63,49,73,50,95,89,43,62,24,88,88,36,6,16,14,2,42,42,60,25,4,58,23,22,27,26,3,79,64,20,92]
	print(Solution().maxNumOfMarkedIndices(nums))