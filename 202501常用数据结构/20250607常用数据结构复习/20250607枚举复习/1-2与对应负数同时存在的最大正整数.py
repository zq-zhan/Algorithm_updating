class Solution:
	def findMaxK(self, nums):
		ans = -1
		set_win = set()
		for x in nums:
			if -x in set_win:
				ans = max(ans, abs(x))
			set_win.add(x)
		return ans
	
if __name__ == '__main__':
	nums = [-1,10,6,7,-7,1]
	print(Solution().findMaxK(nums))