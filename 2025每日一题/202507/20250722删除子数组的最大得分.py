class Solution:
	def maximumUniqueSubarray(self, nums):
		set_win = set()
		ans = temp_s = left = 0
		for right, x in enumerate(nums):
			temp_s += x
			while x in set_win:
				set_win.remove(nums[left])
				temp_s -= nums[left]
				left += 1
			set_win.add(x)
			ans = max(ans, temp_s)
		return ans


if __name__ == '__main__':
	nums = [4,2,4,5,6]
	print(Solution().maximumUniqueSubarray(nums))