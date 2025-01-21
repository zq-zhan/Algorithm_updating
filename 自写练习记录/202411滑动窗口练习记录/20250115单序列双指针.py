# 相向双指针
# 1.反转字符串
class Solution1:
	def reverseString(self, s):
		left, right = 0, n - 1
		while left < right:
			temp = s[left]
			s[left] = s[right]
			s[right] = temp
			left += 1
			right -= 1
		return s
# 数组中的k个最强值
class Solution1:
	def getStrongest(self, arr, k):
		arr.sort()
		n = len(arr)
		med = arr[(n - 1) / 2]
		left, right = 0, n - 1
		ans = []
		while len(ans) < k:
			if abs(arr[right] - med) > abs(arr[left] - med):
				ans.append(arr[right])
				left += 1
			else:
				ans.append(arr[left])
				right -= 1
		return ans