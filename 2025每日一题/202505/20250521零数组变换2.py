from itertools import accumulate

# 20250521零数组变换2
class Solution1:
	def minZeroArray(self, nums, queries):
		if sum(nums) == 0:
			return 0
		diff = [0] * (len(nums) + 1)
		ans = 0
		for left, right, val in queries:
			diff[left] -= val
			diff[right + 1] += val
			new_arr = list(accumulate(diff))[:-1]
			ans += 1
			if all(x + y <= 0 for x, y in zip(new_arr, nums)):
				return ans
		return -1
	
## 灵神题解——二分+差分
class Solution2:
	def minZeroArray(self, nums, queries):
		def check(k):
			diff = [0] * (len(nums) + 1)
			for left, right, val in queries[:k]:
				diff[left] -= val
				diff[right + 1] += val
			for x, y in zip(nums, accumulate(diff)):
				if x + y > 0:
					return False
			return True

		n = len(queries)
		left, right = -1, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right if right <= n else -1


## 灵神题解——双指针+差分
class Solution:
    def minZeroArray(self, nums, queries):
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:  # 需要添加询问，把 x 减小
                l, r, val = queries[k]
                diff[l] += val
                diff[r + 1] -= val
                if l <= i <= r:  # x 在更新范围中
                    sum_d += val
                k += 1
            if sum_d < x:  # 无法更新
                return -1
        return k

	
if __name__ == '__main__':
	nums = [4,3,2,1]
	queries = [[1,3,2],[0,2,1]]
	print(Solution().minZeroArray(nums, queries))