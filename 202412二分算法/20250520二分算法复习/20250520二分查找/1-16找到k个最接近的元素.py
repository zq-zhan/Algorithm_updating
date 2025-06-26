from bisect import bisect_left, bisect_right

class Solution1:
	def findClosestElements(self, arr, k, x):
		range_num = max(x - arr[0], arr[-1] - x)
		for target in range(1, range_num + 2):
			find_left = bisect_left(arr, x - target)
			find_right = bisect_right(arr, x + target)
			if min(find_right, len(arr) - 1) - find_left == k:
				return arr[find_left:find_right + 1][:k]

class Solution:  # O(n) 双指针
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
	arr = [1,1,2,2,2,2,2,3,3]
	k = 3
	x = 3
	print(Solution1().findClosestElements(arr, k, x))