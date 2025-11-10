from math import gcd, lcm

class Solution:
	def replaceNonCoprimes(self, nums):
		def lcm(x, y):
			return abs(x * y) // gcd(x, y)
		# def trans(arr):
		ans = []
		pre = nums[0]
		for y in nums[1:]:
			temp_cal = gcd(pre, y)
			if temp_cal > 1:
				pre = lcm(pre, y)
			else:
				while ans and gcd(ans[-1], pre) > 1:
					pre = lcm(ans[-1], pre)
					ans.pop()
				ans.append(pre)
				pre = y
		while ans and gcd(ans[-1], pre) > 1:
			pre = lcm(ans[-1], pre)
			ans.pop()
		ans.append(pre)
		return ans

## 灵神思路
class Solution:
	def replaceNonCoprimes(self, nums):
		st = []
		for x in nums:
			while st and gcd(x, st[-1]) > 1:
				x = lcm(x, st.pop())
			st.append(x)
		return st


if __name__ == '__main__':
	nums = [8303,361,8303,361,437,361,8303,8303,8303,6859,19,19,361,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,1271,31,961,31,7,2009,7,2009,2009,49,7,7,8897,1519,31,1519,217]
	print(Solution().replaceNonCoprimes(nums))