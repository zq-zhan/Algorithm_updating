# 5.下标对中的最大距离
class Solution1:  # 适用于计数
	def maxDistance(self,nums1,nums2):
		# nums2.sort()
		n = len(nums1)
		m = len(nums2)
		p1 = n-1
		p2 = m-1
		ans = 0
		while p1 > p2:
			p1 -= 1
		while p1 >= 0:
			while p2 >= p1 and p1>=0:
				if nums1[p1] <= nums2[p2]:
					ans = max(ans,p2-p1) 
					p1 -= 1
				else:
					p2 -= 1
					# p1 -= 1
			p1 -= 1
		return ans

# 思路二：复杂度：O(n+m)
class Solution2:
	def maxDistance(self,nums1,nums2):
		n,m = len(nums1),len(nums2)
		ans = 0
		right=0
		for left in range(n):
			right = max(left,right)
			while right < m and nums2[right] >= nums1[left]:
				right += 1
			ans = max(ans,right-left-1)
		return ans

## 思路三：
class Solution3:
    def maxDistance(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        l, r = 0, 0
        res = 0
        while l < m and r < n:
            while r < n and nums2[r] >= nums1[l]:
                res = max(res, r - l)
                r += 1
            l += 1
        
        return res
	
class Solution4:
	def maxDistance(self,nums1,nums2):
		# nums2.sort()
		n = len(nums1)
		m = len(nums2)
		p1 = n-1
		p2 = m-1
		ans = 0
		# while p1 > p2:
		# 	p1 -= 1
		while p1 >= 0 and p2 >=0:
			if nums1[p1] <= nums2[p2]:
				ans = max(ans,p2-p1) 
				p1 -= 1
			else:
				p2 -= 1
					# p1 -= 1
			# p1 -= 1
		return ans

if __name__ == '__main__':
	nums1 = [2,2,2]
	nums2 = [10,10,1]
	s = Solution4()
	print(s.maxDistance(nums1,nums2))