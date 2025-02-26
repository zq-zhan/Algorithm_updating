# 6.两个数组间的距离值
from bisect import bisect_left, bisect_right

class Solution1:
	def findTheDistanceValue(self,arr1,arr2,d):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = 0
		for x in arr1:
			new_arr = []
			new_arr = [-abs(x - y) for y in arr2]
			new_arr.sort()
			find = lower_bound(new_arr,-d)
			if find == len(new_arr):
				ans += 1
			else:
				continue
		return ans
	
class Solution2:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		ans = 0
		p1 = p2 = 0
		n, m = len(arr1), len(arr2)
		while p1 < n:
			while p2 < m:
				if arr1[p1] - arr2[p2] > d:
					p2 += 1
				elif arr1[p1] - arr2[p2] < -d:
					ans += 1
					break
				else:
					break
			if p2 == m:
				ans += n - p1
				break
			p1 += 1
		return ans
	
class Solution3:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()
		ans = 0
		for x in arr1:
			left = bisect_left(arr2, x - d)
			if left == len(arr2) or arr2[left] > d + x :
				ans += 1
		return ans
	
class Solution4:
	def findTheDistanceValue(self, arr1, arr2, d):
		ans = 0
		for x in arr1:
			nums = [abs(x - c) for c in arr2]
			if sum(t > d for t in nums) == len(arr2):
				ans += 1
		return ans

class Solution5:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()
		ans = 0
		for x in arr1:
			start = bisect_left(arr2, x - d)
			# end = bisect_right(arr2, x + d) - 1
			if start >= len(arr2) or arr2[start] > x - d:
				ans += 1
		return ans
## 灵神双指针写法
class Solution6:
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
	cls = Solution6()
	print(cls.findTheDistanceValue(arr1,arr2,d))