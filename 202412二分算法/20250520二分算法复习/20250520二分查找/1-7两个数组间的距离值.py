class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		ans = 0
		for x in arr1:
			new_arr = [abs(x - y) for y in arr2]
			new_arr.sort()
			temp = lower_bound(new_arr, d + 1)
			ans += int(temp == 0)
		return ans
## 灵神题解1:排序+二分查找
class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()
		ans = 0
		for x in arr1:
			i = bisect_left(arr2, x - d)
			if i == len(arr2) or arr2[i] > x + d:
				ans += 1
		return ans
## 灵神题解2:排序+双指针
'''关键思路：利用两个数组的排序找到指针变化的单调性'''
class Solution2:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr1.sort()
		arr2.sort()
		ans = j = 0
		for x in arr1:
			while j < len(arr2) and arr2[j] < x - d:
				j += 1
			if j == len(arr2) or arr2[j] > x + d:
				ans += 1
		return ans

	
if __name__ == '__main__':
	arr1 = [4,5,8]
	arr2 = [10,9,1,8]
	d = 2
	print(Solution2().findTheDistanceValue(arr1, arr2, d))