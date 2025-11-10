class Solution:
	def smallestNumber(self, n):
		while True:
			trans_bin = bin(n)[2:]
			if trans_bin.count('1') == len(trans_bin):
				return n
			n += 1
			
if __name__ == '__main__':
	n = 5
	print(Solution().smallestNumber(n))