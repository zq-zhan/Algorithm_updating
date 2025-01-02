# 1.最小公共值
class Solution1:
	def getCommon(self, nums1, nums2):
		p1 = p2 = 0
		n, m = len(nums1), len(nums2)
		while p1 < n and p2 < m:
			if nums1[p1] < nums2[p2]:
				p1 += 1
			elif nums1[p1] > nums2[p2]:
				p2 += 1
			else:
				return nums1[p1]
		return -1

# 2.合并两个有序数组
class Solution1:
	def merge(self, nums1, m, nums2, n):
		p1 = m - 1
		p2 = n - 1
		i = n + m -1
		while p2 >= 0:
			if p1 >= 0 and nums1[p1] > nums2[p2]:
				nums1[i] = nums1[p1]
				# i -= 1
				p1 -= 1
			else:
				nums1[i] = nums2[p2]
				# i -= 1
				p2 -= 1
			i -= 1

		return nums1

# 3.合并两个二维数组-求和法
class Solution1:
	def mergeArrays(self, nums1, nums2):
		p1 = p2 = 0
		n, m = len(nums1), len(nums2)
		ans = []
		while p1 < n or p2 < m:
			if p1 < n and p2 < m:
				if nums1[p1][0] < nums2[p2][0]:
					ans.append(nums1[p1])
					p1 += 1
				elif nums1[p1][0] > nums2[p2][0]:
					ans.append(nums2[p2])
					p2 += 1
				else:
					ans.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
					p1 += 1
					p2 += 1
			elif p1 >= n:
				ans.append(nums2[p2])
				p2 += 1
			elif p2 >= m:
				ans.append(nums1[p1])
				p1 += 1
		return ans


