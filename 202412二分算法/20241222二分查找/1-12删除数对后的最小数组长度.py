# 12.删除数对后的最小数组长度
from bisect import bisect_left,bisect_right


class Solution1:
	def minLengthAfterRemovals(self,nums):
		# nums_dic = Counter(nums)
		n = len(nums)
		target = nums[n // 2]
		max_cnt = bisect_right(nums, target) - bisect_left(nums, target)
		return max(2 * max_cnt - n, n % 2)
	
if __name__ == '__main__':
	nums = [1,2,3,4]
	cls = Solution1()
	print(cls.minLengthAfterRemovals(nums))