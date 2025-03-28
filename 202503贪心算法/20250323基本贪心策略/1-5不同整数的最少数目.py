# 5.不同整数的最少数目
from collections import Counter

class Solution1:
	def findLeastNumOfUniqueInts(self, arr, k):
		arr = Counter(arr)
		n = len(arr)
		arr = sorted(arr.items(), key = lambda item: item[1])
		for i, (key, value) in enumerate(arr, 1):
			k -= value
			if k == 0:
				return n - i
			elif k < 0:
				return n - i + 1
		return 0
	
## 写法2
class Solution2:
	def findLeastNumOfUniqueInts(self, arr, k):
		arr = list(Counter(arr).values())
		arr.sort()
		while k > 0:
			if k >= arr[0]:
				k -= arr.pop(0)
			else:
				k = 0
		return len(arr)
	
if __name__ == '__main__':
	arr = [5,5,4]
	k = 1
	print(Solution2().findLeastNumOfUniqueInts(arr, k))