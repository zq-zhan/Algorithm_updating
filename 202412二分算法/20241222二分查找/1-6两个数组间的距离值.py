# 6.两个数组间的距离值
from bisect import bisect_left

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

if __name__ == '__main__':
	arr1 = [1,4,2,3]
	arr2 = [-4,-3,6,10,20,30]
	d = 3
	cls = Solution3()
	print(cls.findTheDistanceValue(arr1,arr2,d))