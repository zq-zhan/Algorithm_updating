# 2.合并两个有序数组
class Solution1:
	def merge(self,nums1,m,nums2,n):
		i = m - 1 
		j = n - 1 
		k=m + n - 1
		while k >= 0:
			if i >= 0 and j >= 0:
				if nums2[j] > nums1[i]:
					nums1[k] = nums2[j]
					k -= 1
					j -= 1
				elif nums2[j] < nums1[i]:
					nums1[k] = nums1[i]
					i -= 1
					k -= 1
				else:
					nums1[k], nums1[k-1] = nums1[i], nums2[j]
					k -= 2
					i -= 1
					j -= 1
			elif i < 0:
				nums1[k] = nums2[j]
				j -= 1
				k -= 1
			else:
				nums1[k] = nums1[i]
				i -= 1
				k -= 1
		return nums1 
	
## 
class Solution2:
	def merge(self,nums1,m,nums2,n):
		p1, p2, p = m-1, n-1, m+n-1
		while p2 >= 0:  # 只需要把nums2迭代完即可，若nums2为空，则直接返回nums1
			if p1 >= 0 and nums1[p1] > nums2[p2]:
				nums1[p] = nums1[p1]
				p1 -= 1
			else:
				nums1[p] = nums2[p2]
				p2 -= 1
			p -= 1
		return nums1

class Solution3:
	def merge(self, nums1, m, nums2, n):
		p1 = m - 1
		p2 = n - 1
		i = n + m -1
		while p1 >= 0 and p2 >= 0:
			if nums1[p1] > nums2[p2]:
				nums1[i] = nums1[p1]
				i -= 1
				p1 -= 1
			elif nums1[p1] < nums2[p2]:
				nums1[i] = nums2[p2]
				i -= 1
				p2 -= 1
		if p1 > 0:
			nums1[:i] = nums1[:p1 + 1]
		elif p2 > 0:
			nums1[:i] = nums2[:p2 + 1]
		return nums1
	
if __name__ == '__main__':
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3
	s = Solution3()
	print(s.merge(nums1,m,nums2,n))