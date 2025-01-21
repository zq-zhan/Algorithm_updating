# 1.区域和检索-数组不可变
class NumArray:
	def __init__(self, nums):
		self.nums = nums
		pre_nums = [0]
		for i in range(0, len(nums)):
			pre_nums.append(nums[i] + pre_nums[-1])
		self.pre_nums = pre_nums

	def sumRange(self, left, right):
		return self.pre_nums[right] - self.pre_nums[left - 1]

# 2.统计范围内的元音字符串数
class Solution1:
	def vowelStrings(self, words, queries):
		suf_vowels = [0]
		for word in words:
			cnt = 1 if word[0] in 'aeiou' and word[-1] in 'aeiou' else 0
			suf_vowels.append(suf_vowels[-1] + cnt)
		ans = []
		for left,right in queries:
			ans.append(suf_vowels[right + 1] - suf_vowels[left])
		return ans

# 3.和有限的最长子序列
class Solution1:  # 这个解法是子数组！！！
	def answerQueries(self, nums, queries):
		nums.sort()  # 注意！！！
		suf_sum = [0]
		for x in nums:
			suf_sum.append(suf_sum[-1] + x)
		# suf_sum.append(suf_sum[-1] + nums[-1])
		n = len(suf_sum)

		ans = []
		for target in queries:
			temp = 0
			left = 0
			for right in range(1, n):
				if suf_sum[right] - suf_sum[left] <= target:
					temp = max(temp, right - left)
					# right += 1
					continue
				left += 1
			ans.append(temp)
		return ans
## 前缀和+二分查找
class Solution2:
	def answerQueries(self, nums, queries):
		nums.sort()
		n = len(nums)
		for i in range(1, n):
			nums[i] += nums[i - 1]
		ans = []
		for target in queries:
			ans.append(bisect_right(nums, target))
		return ans

# 4.特殊数组2
class Solution1:
	def isArraySpecial(self, nums, queries):
		pre_lis = [0, 1]
		for p1 in range(2, len(nums)):
			if nums[p1] % 2 != nums[p1 - 1] % 2:
				pre_lis.append(pre_lis[-1] + 1)
			else:
				pre_lis.append(pre_lis[-1] - 1)
		ans = []
		for left, right in queries:
			if right - left == 0:
				ans.append(False)
			elif pre_lis[right + 1] - pre_lis[left] == right - left + 1:
				ans.append(True)
			else:
				ans.append(False)
		return False
## 灵神题解
class Solution2:
	def isArraySpecial(self, nums, queries):
		a_lis = []  # 长度为n - 1
		for p1 in range(len(nums)):
			if nums[p1] % 2 != nums[p1 + 1] % 2:
				a_lis.append(0)
			else:
				a_lis.append(-1)
		pre_a_sum = [0]
		for x in a_lis:
			pre_a_sum.append(pre_a_sum[-1] + x)

		ans = []
		for left, right in queries:
			if pre_a_sum[right] == pre_a_sum[left]:
				ans.append(True)
			else:
				ans.append(False)
		return ans
class Solution3:
	def isArraySpecial(self, nums, queries):
		s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), initial = 0))
		return [s[right] == s[left] for left, right in queries]

# 5.任意子数组和的绝对值的最大值
class Solution1:
	def maxAbsoluteSum(self, nums):
		# 转换为在前缀和数组中找和最大的子数组
		pre_sum = [0]
		for p1 in range(len(nums)):
			pre_sum.append(pre_sum[-1] + nums[p1])
		# ans = 0
		# for i in range(len(pre_sum)):
		# 	for j in range(len(pre_sum)):
		# 		ans = max(abs(pre_sum[j] - pre_sum[i]), ans)
		return max(pre_sum) - min(pre_sum)
## 滑动窗口思路
class Solution2:
	def maxAbsoluteSum(self, nums):
		def max_sum(max_num, new_arr):
			ans = max_num
			left = 0
			dic_sum = 0
			for right, c in enumerate(new_arr):
				dic_sum += c
				if dic_sum >= ans:
					# dic_sum += c
					ans = max(dic_sum,ans)
					continue
				dic_sum -= new_arr[left]
				left = right
			return ans
		ans = max_sum(0, nums)
		nums = [-x for x in nums]
		ans = max_sum(ans, -nums)
		return ans
	
# 6.二的幂数组中查询范围内的乘积
class Solution1:
	def productQueries(self, n, queries):
		target = int(log2(n + 1))
		ori_arr = [2 ** x for x in range(target + 1)]
		temp_sum = 0
		# new_arr = []
		min_arr = [0] * len(ori_arr)
		left = 0
		for right, c in enumerate(ori_arr):
			temp_sum += c
			while sum(new_arr) >= n:
				if temp_sum == n and right - left + 1 < len(min_arr):
					min_arr = ori_arr[left: right + 1]
				temp_sum -= ori_arr[left]
				left += 1

		sub_plus = [1]
		for p1 in range(len(min_arr)):
			sub_plus.append(sub_plus[-1] * min_arr[p1])

		ans = []
		for left, right in queries:
			ans.append(sub_plus[right + 1] // sub_plus[left])
		return ans
## 
class Solution2:
	def productQueries(self, n, queries):
		target = int(log2(n + 1))
		ori_arr = [2 ** x for x in range(target + 1)]
		temp_diff = n
		min_arr = []
		while temp_diff > 0:
			min_arr.append(max([x for x in ori_arr if x <= temp_diff]))
			temp_diff -= min_arr[-1]

		p1, p2 = 0, len(min_arr) - 1
		while p1 < p2:
			temp = min_arr[p1]
			min_arr[p1] = min_arr[p2]
			min_arr[p2] = temp
			p1 += 1
			p2 -= 1

		# temp_sum = 0
		# # new_arr = []
		# min_arr = [0] * len(ori_arr)
		# left = 0
		# for right, c in enumerate(ori_arr):
		# 	temp_sum += c
		# 	while sum(new_arr) >= n:
		# 		if temp_sum == n and right - left + 1 < len(min_arr):
		# 			min_arr = ori_arr[left: right + 1]
		# 		temp_sum -= ori_arr[left]
		# 		left += 1
        
		sub_plus = [1]
		for p1 in range(len(min_arr)):
			sub_plus.append(sub_plus[-1] * min_arr[p1])

		ans = []
		for left, right in queries:
			ans.append(sub_plus[right + 1] // sub_plus[left])
		return ans
## 灵神题解
MOD = 10 ** 9 + 7

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        a = []
        while n:
            lb = n & -n
            a.append(lb)
            n ^= lb
        na = len(a)
        res = [[0] * na for _ in range(na)]
        for i, x in enumerate(a):
            res[i][i] = x
            for j in range(i + 1, na):
                res[i][j] = res[i][j - 1] * a[j] % MOD
        return [res[l][r] for l, r in queries]

# 7.两个字符串的切换距离
class Solution1:
	def shiftDistance(self, s, t, nextCost, previousCost):
		pre_nextCost_sum = [0]
		pre_previousCost_sum = [0]
		for p1 in range(26):
			pre_nextCost_sum.append(pre_nextCost_sum[-1] + nextCost[p1])
			pre_previousCost_sum.append(pre_previousCost_sum[-1] + previousCost[p1])

		ans = 0
		for i in range(len(s)):
			# forward = sum(pre_nextCost_sum) - (pre_nextCost_sum[ord(t[i]) - ord('a')] - pre_nextCost_sum[ord(s[i]) - ord('a')])
			back = pre_nextCost_sum[ord(t[i]) - ord('a')] - pre_nextCost_sum[ord(s[i]) - ord('a')]
			if sum(pre_previousCost_sum) >= 2 * back:
				ans += diff
			else:
				ans += sum(pre_nextCost_sum) - back
		return ans
## 灵神题解
class Solution2:
	def shiftDistance(self, s, t, nextCost, previousCost):
		sigma = 26
		nxt_sum = [0] * (sigma * 2 + 1)
		pre_sum = [0] * (sigma * 2 + 1)
		for i in range(sigma * 2):
			nxt_sum[i + 1] = nxt_sum[i] + nextCost[i % sigma]
			pre_sum[i + 1] = pre_sum[i] + previousCost[i % sigma]

		ans = 0
		ord_a = ord('a')
		for x, y in zip(s, t):
			x = ord(x) - ord_a
			y = ord(y) - ord_a
			ans += min(
				nxt_sum[y + sigma if y < x else y] - nxt_sum[x],
				pre_sum[(x + sigma if x < y else x) + 1] - pre_sum[y + 1]
				)
		return ans


##############################################
# 前缀和与哈希表
# 1.和相同的二元子数组
class Solution1:
	def numSubarraysWithSum(self, nums, goal):
		temp_sum = ans = 0
		left = 0
		for right, c in enumerate(nums):
			temp_sum += c
			if temp_sum < goal:
				continue

			while temp_sum >= goal:
				ans += 1 if temp_sum == goal
				temp_sum -= nums[left]
				left += 1
			# ans += 1
		return ans
## 恰好型滑动窗口
class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		def max_win(target):
			temp_ans = temp_sum = 0
			left = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					# temp_ans += left
					temp_sum -= nums[left]
					left += 1
				temp_ans += left
		return max_sum(goal) - max_sum(goal + 1)
				
# 2.和为K的子数组
class Solution1:
	def subarraySum(self, nums, k):
		def max_sum(target):
			temp_ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					temp_sum -= nums[left]
					left += 1
				temp_ans += 1
			return temp_ans
		return max_sum(k) - max_sum(k + 1)
## 灵神题解
class Solution1:
	def subarraySum(self, nums, k):
		s = [0]
		for i, x in enumerate(nums):
			s[i + 1] = s[i] + x

		ans = 0
		cnt = defaultdict(int)
		for sj in s:
			ans += cnt[sj - k]
			cnt[sj] += 1
		return ans

