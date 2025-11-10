class Solution:
	def makeTheIntegerZero(self, num1, num2):
		for k in range(1, 61):  # k 不会超过 60（因为 2^60 已经非常大）
			x = num1 - k * num2
			if x < k:
				continue
			# if x.bit_count() <= k:
			if bin(x).count("1") <= k:
				return k
		return -1
     
if __name__ == '__main__':
	s = Solution()
	print(s.makeTheIntegerZero(3, -2))  # 2