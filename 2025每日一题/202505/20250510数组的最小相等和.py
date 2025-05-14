class Solution1:
	def minSum(self, nums1, nums2):
		temp_s1 = sum(nums1)
		cnt_1 = nums1.count(0)

		temp_s2 = sum(nums2)
		cnt_2 = nums2.count(0)


		if cnt_1 > 0 and cnt_2 > 0:
			return max(temp_s1 + cnt_1, temp_s2 + cnt_2)
		elif cnt_1 > 0:
			if temp_s1 >= temp_s2:
				return -1
			else:
				if cnt_1 > temp_s2 - temp_s1:
					return -1
				else:
					return temp_s2
		elif cnt_2 > 0:
			if temp_s2 >= temp_s1:
				return -1
			else:
				if cnt_2 > temp_s1 - temp_s2:
					return -1
				else:
					return temp_s1
		else:
			if temp_s1 == temp_s2:
				return temp_s1
			else:
				return -1
			
## 优化题解
class Solution2:
	def minSum(self, nums1, nums2):
		s1, c1 = sum(nums1), nums1.count(0)
		s2, c2 = sum(nums2), nums2.count(0)

		b1 = s1 + c1
		b2 = s2 + c2
		t = max(b1, b2)

		if (c1 == 0 and b1 < t) or (c2 == 0 and b2 < t):
			return -1
		return t

	
if __name__ == '__main__':
	# nums1 = [0,7,28,17,18]
	# nums2 = [1,2,6,26,1,0,27,3,0,30]
	nums1 = [2,0,2,0]
	nums2 = [1,4]
	print(Solution1().minSum(nums1, nums2))