# 20250403有序三元组中的最大值2
class Solution1:
	def maximumTripletValue(self, nums):
		ans = maxPre = maxDiff = 0
		for x in nums:
			ans = max(x * maxDiff, ans)
			maxPre = max(maxPre, x)
			maxDiff = max(maxDiff, maxPre - x)
		return ans
	
if __name__ == '__main__':
	nums = [12,6,1,2,7]
	print(Solution1().maximumTripletValue(nums))