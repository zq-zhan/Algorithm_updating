# 6.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		p1 = p2 = 0
		n = len(arr1)
		m = len(arr2)
		ans = 0
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
				ans += n-p1
				break
			p1 += 1
		return ans
## 灵神思路
class Solution2:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		ans = j =0
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
	s = Solution3()
	print(s.findTheDistanceValue(arr1,arr2,d))