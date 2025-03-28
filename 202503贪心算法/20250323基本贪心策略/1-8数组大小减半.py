from collections import Counter

# 8.数组大小减半
class Solution1:
	def minSetSize(self, arr):
		n = len(arr) // 2
		new_arr = sorted(Counter(arr).values(), reverse = True)
		for i, x in enumerate(new_arr, 1):
			n -= x
			if n <= 0:
				return i
			
if __name__ == '__main__':
	arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
	print(Solution1().minSetSize(arr))