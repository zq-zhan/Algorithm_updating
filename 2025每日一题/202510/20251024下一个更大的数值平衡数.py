from collections import Counter

class Solution:
	def nextBeautifulNumber(self, n):
		while True:
			n += 1
			cnt = Counter(str(n))
			if all(int(d) == c for d, c in cnt.items()):
				return n
			
if __name__ == '__main__':
	n = 3000
	print(Solution().nextBeautifulNumber(n))