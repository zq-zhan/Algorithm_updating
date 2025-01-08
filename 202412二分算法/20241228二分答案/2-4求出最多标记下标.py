# 4.求出最多标记下标

class Solution1:
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		# left, right = -1, len(nums) 
		p2 = len(nums) - 1
		ans = 0
		mid = (len(nums) - 1) // 2
		# while left + 1 < right:
			# mid = (left + right) // 2
		while mid >= 0 and p2 > (len(nums) - 1) // 2:
			if nums[mid] * 2 <= nums[p2]:
				mid -= 1
				p2 -= 1
				ans += 2
			else:
				mid -= 1
		return ans

## 灵神思路——二分法
class Solution2:
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		left, right = 0, len(nums) // 2 + 1  # 二分答案，答案区间在[0, len(nums)//2]中
		n = len(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			# if all(nums[i] * 2 <= nums[i - mid] for i in range(mid)):
			if all(nums[i] * 2 <= nums[n - mid + i] for i in range(mid)):
				left = mid
			else:
				right = mid
		return left * 2
	
if __name__ == '__main__':
	nums = [57,40,57,51,90,51,68,100,24,39,11,85,2,22,67,29,74,82,10,96,14,35,25,76,26,54,29,44,63,49,73,50,95,89,43,62,24,88,88,36,6,16,14,2,42,42,60,25,4,58,23,22,27,26,3,79,64,20,92]
	cls = Solution2()
	print(cls.maxNumOfMarkedIndices(nums))