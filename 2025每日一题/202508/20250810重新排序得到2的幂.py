class Solution:
	def reorderedPowerOf2(self, n):
		diff = n - 1
		diff = list(str(diff))
		n = list(str(n))
		diff = int(''.join(diff))
		n = int(''.join(n))
		return True if n & diff == 0 else False
	
if __name__ == '__main__':
	n = 46
	print(Solution().reorderedPowerOf2(n))