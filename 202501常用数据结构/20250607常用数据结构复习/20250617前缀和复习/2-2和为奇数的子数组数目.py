from collections import defaultdict

class Solution:
	def numOfSubarrays(self, arr):
		mod = 10 ** 9 + 7
		dic_win = defaultdict(int)
		dic_win[0] = 1
		ans = temp_s = 0
		for x in arr:
			temp_s += x
			ans += dic_win[1 - temp_s % 2]
			dic_win[1 - temp_s % 2] += 1
		return ans % mod
	
if __name__ == '__main__':
	arr = [1,3,5]
	print(Solution().numOfSubarrays(arr))