# 1.最小公共值
from math import inf


class Solution1:
	def getCommon(self,nums1,nums2):
		# ans=inf
		i=0
		j=0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				i+=1
			elif nums1[i] > nums2[j]:
				j+=1
			else:
				# ans=nums1[i]
				return nums1[i]
				# break
		return -1
	
## 灵神思路
class Solution2:
	def getCommon(self,nums1,nums2):
		j,m=0,len(nums2)
		for x in nums1:
			while j<m and nums2[j]<x:
				j+=1
			if j<m and nums2[j]==x:
				return x
		return -1

if __name__ == '__main__':
	nums1=[1,2,3,4,5]
	nums2=[6,7,8,9,10]
	s=Solution2()
	print(s.getCommon(nums1,nums2))

