class Solution1:
	def findClosestElements(self, arr, k, x):
		n = len(arr)
		left, right = 0, n - 1
		while right - left + 1 > k:
			a = arr[left]
			b = arr[right]
			if abs(a - x) > abs(b - x):
				left += 1
			elif abs(a - x) < abs(b - x):
				right -= 1
			else:
				right -= 1
		return arr[left: right + 1]
	
if __name__ == '__main__':
	arr = [1,2,3,4,5]
	k = 4
	x = 3
	print(Solution1().findClosestElements(arr, k, x))