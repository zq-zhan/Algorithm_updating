# 14.最大得分
class Solution1:
	def maxSum(self,nums1,nums2):
		p1 = p2 = 0
		n, m = len(nums1), len(nums2)
		ans = 0
		total_p1 = 0
		total_p2 = 0
		i = j = 0
		same_lis = []
		while i < n and j < m:
			if nums1[i] < nums2[j]:
				i += 1
			elif nums1[i] > nums2[j]:
				j += 1
			else:
				same_lis.append(nums1[i])
				i += 1
				j += 1
		k = 0
		# latest_point = 0
		while p1 < n or p2 < m:
			if p1 < n:
				if k == len(same_lis):
					total_p1 += nums1[p1]
					p1 += 1
				elif nums1[p1] < same_lis[k]:
					total_p1 += nums1[p1]
					p1 += 1
			if p2 < m:
				if k == len(same_lis):
					total_p2 += nums2[p2]
					p2 += 1
				elif nums2[p2] < same_lis[k]:
					total_p2 += nums2[p2]
					p2 += 1
			flag = 1

			if p1 < n and p2 < m and nums1[p1] == nums2[p2]:
				ans += max(total_p1+same_lis[k],total_p2+same_lis[k])
				total_p1 = 0
				total_p2 = 0
				k += 1
				flag = 0
				p1 += 1
				p2 += 1
		

		if flag:
			ans += max(total_p1, total_p2)
		return ans%(10**9+7)

class Solution2:
    def maxSum(self, nums1, nums2) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        sum1 = 0
        sum2 = 0
        while i < n1 or j < n2:
            if (i < n1) and (j >= n2 or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            elif (j < n2) and (i >= n1 or nums1[i] > nums2[j]):
                sum2 += nums2[j]
                j += 1
            else:
                sum1 = sum2 = max(sum1,sum2) + nums1[i]
                i += 1
                j += 1

        return int(max(sum1,sum2) % (1e9+7))


if __name__ == '__main__':
	nums1 = [2,4,5,8,10]
	nums2 = [4,6,8,9]
	s = Solution2()
	print(s.maxSum(nums1,nums2))