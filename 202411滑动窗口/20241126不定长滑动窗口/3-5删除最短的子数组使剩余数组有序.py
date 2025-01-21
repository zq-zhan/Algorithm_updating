# 5.删除最短的子数组使剩余数组有序
class Solution1:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		ans = n
		left = 0
		ans_lis = [arr[0]]
		for right, c in enumerate(arr):
			if c >= ans_lis[-1]:
				ans_lis.append(c)
				left += 1
				continue
## 灵神题解
### 方法一：枚举左端点left，移动右端点right，直到arr[left]<=arr[right]
class Solution2:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		right = n - 1
		while right and arr[right - 1] <= arr[right]:
			right -= 1
		if right == 0:
			return 0

		ans = right  # 删除arr[:right]
		left = 0
		while left == 0 or arr[left - 1] <= arr[left]:
			while right < n and arr[right] < arr[left]:
				right += 1
			ans = min(ans, right - left - 1)  # arr[left] <= arr[right],删除arr[left+1:right]
			left += 1
		return ans
### 方法二：枚举右端点right，移动左端点，直到arr[left]>arr[right]
class Solution3:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		right = n - 1
		while right and arr[right - 1] <= arr[right]:
			right -= 1
		if right == 0:
			return 0
		ans = right
		left = 0
		while True:
			while right == n or arr[left] <= arr[right]:
				ans = min(ans, right - left - 1)
				if arr[left] > arr[left + 1]:
					return ans
				left += 1
			right += 1

	
if __name__ == '__main__':
	arr = [1,2,3,10,4,2,3,5]
	cls = Solution3()
	print(cls.findLengthOfShortestSubarray(arr))