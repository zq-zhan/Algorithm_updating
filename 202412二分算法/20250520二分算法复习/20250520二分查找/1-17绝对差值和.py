class Solution1:
	def minAbsoluteSumDiff(self, nums1, nums2):
		mod = 10 ** 9 + 7
		new_lis = []
		n = len(nums1)
		ans = 0
		for i in range(n):
			new_lis.append((i, abs(nums1[i] - nums2[i])))
			ans += abs(nums1[i] - nums2[i])

		new_lis.sort(key = lambda x:x[1])
		k = new_lis[-1][0]

		nums1_set = set(nums1)
		temp_s = ans_ori = ans
		for x in nums1_set:
			temp_s += abs(x - nums2[k]) - abs(nums1[k] - nums2[k])
			ans_ori = min(ans_ori, temp_s)
			temp_s = ans
		return ans_ori % mod

class Solution2:
	def minAbsoluteSumDiff(self, nums1, nums2):
		n = len(nums1)
		st = sorted(nums1)
		s, mx = 0, 0
		for x, y in zip(nums1, nums2):
			if x == y:
				continue
			z = abs(x - y)
			s += z
			left, right = -1, n
			while left + 1 < right:
				mid = (left + right) // 2
				if st[mid] < y:
					left = mid
				else:
					right = mid
			mx = max(mx, z - min(abs(st[right] - y) if right < n else z, abs(st[right - 1] - y) if 0 <= right - 1 <= n - 1 else z))
		return (s - mx) % (10 ** 9 + 7)


if __name__ == '__main__':
	nums1 = [1,28,21]
	nums2 = [9,21,20]
	print(Solution2().minAbsoluteSumDiff(nums1, nums2))