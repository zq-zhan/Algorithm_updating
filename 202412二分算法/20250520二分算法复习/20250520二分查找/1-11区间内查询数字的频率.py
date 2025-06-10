from bisect import bisect_left, bisect_right

class RangeFreqQuery:
	def __init__(self, arr):
		self.arr = arr

	def query(self, left, right, value):
		nums = self.arr[left:right + 1]
		nums.sort()
		return bisect_right(nums, value) - bisect_left(nums, value)

	
if __name__ == '__main__':
	arr = [12,33,4,56,22,2,34,33,22,12,34,56]
	obj = RangeFreqQuery(arr)
	print(obj.query(1, 2, 4)) # Output: 2
	print(obj.query(0, 11, 33)) # Output: 2