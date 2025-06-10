class Solution1:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		ans = 0
		left = right = 0
		while left <= right and right <= n - 1:
			if right > 0 and arr[right] >= arr[right - 1]:
				right += 1
			else:
				left = right  #问题在于这样变化，不能保证left需不需要左移
## 灵神题解
class Solution2:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		right = n - 1
		while right and arr[right - 1] <= arr[right]:
			right -= 1
		if right == 0:
			return 0

		ans = right
		left = 0
		while left == 0 or arr[left - 1] <= arr[left]:
			while right < n and arr[right] < arr[left]:
				right += 1
			ans = min(ans, right - left - 1)
			left += 1
		return ans
	
if __name__ == '__main__':
	arr = [1, 2, 3, 10, 4, 2, 3, 5]
	print(Solution2().findLengthOfShortestSubarray(arr))