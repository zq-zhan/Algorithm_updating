# 3.合并两个二维数组-求和法
class Solution1:
	def mergeArrays(self,nums1,nums2):
		p1 = p2 =0
		n = len(nums1)
		m = len(nums2)
		ans = []
		while p1 < n or p2 < m:
			if p1 < n and p2 < m:
				if nums1[p1][0] < nums2[p2][0]:
					ans.append([nums1[p1][0],nums1[p1][1]])
					p1 += 1
				elif nums1[p1][0] == nums2[p2][0]:
					ans.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
					p1 += 1
					p2 += 1
				else:
					ans.append([nums2[p2][0],nums2[p2][1]])
					p2 += 1
			elif p1 >= n:
				ans.append([nums2[p2][0],nums2[p2][1]])
				p2 += 1
			else:
				ans.append([nums1[p1][0],nums1[p1][1]])
				p1 += 1
		return ans

## 优化
class Solution2:
	def mergeArrays(self,nums1,nums2):
		p1 = p2 =0
		n = len(nums1)
		m = len(nums2)
		ans = []
		while p1 < n and p2 < m:
			if nums1[p1][0] < nums2[p2][0]:
				ans.append(nums1[p1])
				p1 += 1
			elif nums1[p1][0] == nums2[p2][0]:
				nums1[p1][1] += nums2[p2][1]
				ans.append(nums1[p1])
				p1 += 1
				p2 += 1
			else:
				ans.append(nums2[p2])
				p2 += 1
		if p1 < n:
			ans.extend(nums1[p1:])
		if p2 < m:
			ans.extend(nums2[p2:])
		return ans


## 灵神思路
class Solution3:
	def mergeArrays(self,nums1,nums2):
		ans = []
		i, n = 0, len(nums1)
		j, m = 0, len(nums2)
		while True:
			if i == n:
				ans.extend(nums2[j:])
				return ans
			if j == m:
				ans.extend(nums1[i:])
				return ans
			if nums1[i][0] < nums2[j][0]:
				ans.append(nums1[i])
				i += 1
			elif nums1[i][0] > nums2[j][0]:
				ans.append(nums2[j])
				j += 1
			else:
				nums1[i][1] += nums2[j][1]
				ans.append(nums1[i])
				i += 1
				j += 1

if __name__ == '__main__':
	nums1 = [[1,2],[2,3],[4,5],[7,4]]
	nums2 = [[1,4],[3,2],[4,1]]
	s = Solution2()
	print(s.mergeArrays(nums1,nums2))