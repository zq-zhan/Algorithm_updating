from bisect import bisect_left, bisect_right

class Solution1:
	def countFairPairs(self, nums, lower, upper):
		ans = 0
		n = len(nums)
		for i, c in enumerate(nums):
			for j in range(i + 1, n):
				if lower <= c + nums[j] <= upper:
					ans += 1
		return ans
## 优化——灵神题解——二分法
class Solution2:
	def countFairPairs(self, nums, lower, upper):
		nums.sort()
		ans = 0
		for j, c in enumerate(nums):
			right = bisect_right(nums, upper - c, 0, j)  # 从0到j-1之间的元素
			left = bisect_left(nums, lower - c, 0, j)
			ans += right - left
		return ans
class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        l = r = len(nums)
        for j, x in enumerate(nums):
            while r and nums[r - 1] > upper - x:
                r -= 1
            while l and nums[l - 1] >= lower - x:
                l -= 1
            # 在方法一中，二分的结果必须 <= j，方法二同理
            ans += min(r, j) - min(l, j)
        return ans
	
if __name__ == '__main__':
	nums = [0,1,7,4,4,5]
	lower = 3
	upper = 6
	print(Solution().countFairPairs(nums, lower, upper))

