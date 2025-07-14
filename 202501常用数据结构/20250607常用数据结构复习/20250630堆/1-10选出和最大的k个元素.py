import heapq

class Solution:
	def findMaxSum(self, nums1, nums2, k):
		new_arr = [(x, i) for i, x in enumerate(nums1)]
		new_arr.sort(key = lambda x:x[0])

		n = len(nums1)
		ans = []
		for i in range(0, n):
			target = nums1[i]
			target_num = []
			for x, index in new_arr:
				if x < target:
					heapq.heappush(target_num, -nums2[index])
				else:
					break
			temp_s = 0
			for _ in range(k):
				if target_num:
					temp_s += -heapq.heappop(target_num)
				else:
					break
			ans.append(temp_s)
		return ans

## 灵神题解
class Solution:
	def findMaxSum(self, nums1, nums2, k):
		new_arr = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))

		n = len(new_arr)
		ans = [0] * n
		temp_lis = []
		temp_s = i = 0
		while i < n:
			start = i
			target = new_arr[start][0]
			while i < n and new_arr[i][0] == target:
				ans[new_arr[i][2]] = temp_s
				i += 1
			for j in range(start, i):
				y = new_arr[j][1]
				temp_s += y
				heapq.heappush(temp_lis, y)
				if len(temp_lis) > k:
					temp_s -= heapq.heappop(temp_lis)
		return ans

class Solution:
    def findMaxSum(self, nums1, nums2, k):
        a = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))
        n = len(a)
        ans = [0] * n
        h = []
        s = 0
        for i, (x, y, idx) in enumerate(a):
            ans[idx] = ans[a[i - 1][2]] if i and x == a[i - 1][0] else s
            s += y
            heapq.heappush(h, y)
            if len(h) > k:
                s -= heapq.heappop(h)
        return ans

if __name__ == '__main__':
	nums1 = [4,2,1,5,3]
	nums2 = [10,20,30,40,50]
	k = 2
	print(Solution().findMaxSum(nums1, nums2, k))