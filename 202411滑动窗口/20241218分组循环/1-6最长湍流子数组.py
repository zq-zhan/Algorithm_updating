# 6.最长湍流子数组
class Solution1:
	def maxTurbulenceSize(self,arr):
		ans = 1
		left, right = 0, 2
		while right < len(arr):
			if (arr[right-2] >= arr[right - 1] and arr[right - 1] >= arr[right]) or (arr[right-2] <= arr[right - 1] and arr[right - 1] <= arr[right]):
				if arr[right-2] == arr[right-1] == arr[right]:
					ans = max(ans, 1)
				# elif arr[right-1] == arr[right]:
				# 	ans = max(ans, 2)
				else:
					ans = max(ans,right - left)
				left = right - 1
			right += 1
		if len(arr) == 1 or (len(arr) >= 2 and arr[right-2] == arr[right-1]):
			ans = max(ans, 1)
		else:
			ans = max(ans,right - left)
		return ans
	
if __name__ == '__main__':
	# arr = [9,4,2,10,7,8,8,1,9]
	arr = [100,100,100]
	# arr = [4,8,12,16]
	s = Solution1()
	print(s.maxTurbulenceSize(arr))