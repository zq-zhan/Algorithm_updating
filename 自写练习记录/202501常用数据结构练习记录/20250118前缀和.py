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
class Solution1:  # 错解
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
class Solution2:
	def subarraySum(self, nums, k):
		s = [0] * (len(nums) + 1)
		for i, x in enumerate(nums):
			s[i + 1] = s[i] + x

		ans = 0
		cnt = defaultdict(int)  # 记录前缀和出现的次数
		for sj in s:
			ans += cnt[sj - k]  # 统计在j左边（即出现在已遍历的前缀和中）使得s[j] - s[i] = k 即和为k的子数组个数
			cnt[sj] += 1  # 更新前缀和出现的次数
		return ans
## 灵神题解——方法二：一次遍历
class Solution3:
	def subarraySum(self, nums, k):
		ans = pre_sum = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		for i, c in enumerate(nums):
			pre_sum += c
			ans += cnt[pre_sum - k]
			cnt[pre_sum] += 1
		return ans

# 3.和为奇数的子数组数目
class Solution1:
	def numOfSubarrays(self, arr):
		pre_sum = [0] * (len(arr) + 1)
		for i, c in enumerate(arr):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for pre_s in pre_sum:
			ans += cnt[1 - pre_s % 2]
			ans += 1 if pre_s % 2 == 1
			cnt[pre_s % 2] += 1
		return ans % (10 ** 9 + 7)
## 
class Solution2:
	def numOfSubarrays(self, arr):
		pre_sum = [0] * (len(arr) + 1)
		for i, c in enumerate(arr):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for pre_s in pre_sum:
			ans += cnt[(pre_s % 2)^1]
			# ans += 1 if pre_s % 2 == 1
			cnt[pre_s % 2] += 1
		return ans % (10 ** 9 + 7)

class Solution:
    def numOfSubarrays(self, arr):
        s=[0]*(len(arr)+1)
        for i,x in enumerate(arr):
            s[i+1]=s[i]+x
        mod=10**9+7
        ans=0
        cnt=[0]*2
        for sj in s:
            ans+=cnt[(sj%2)^1]
            cnt[(sj%2)]+=1
        return ans%mod

# 4.和可被k整除的子数组数目
## 思路：前缀和的差值可以被k整除—— 不同前缀和对k取模结果相等
class Solution1:
	def subarraysDivByK(self, num, k):
		pre_sum = [0] * (len(nums) + 1)
		for i, c in enumerate(nums):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for sj in pre_sum:
			ans += cnt[sj % k]
			cnt[sj % k] += 1
		return ans

# 5.连续的子数组和
class Solution1:
	def checkSubarraySum(self, nums, k):
		temp_sum = 0
		left = 0
		for right, c in enumerate(nums):
			temp_sum += c
			if right - left + 1 < 2:
				continue
			while right - left + 1 >= 2 and temp_sum % k == 0:
				return True
		return False

class Solution2:
	def checkSubarraySum(self, nums, k):
		pre_sum = [0] * (len(nums) + 1)
		for i, c in enumerate(nums):
			pre_sum[i + 1] = pre_sum[i] + c

		# pre_sum = [nums[0]]
		# for i in range(1, len(nums)):
		# 	pre_sum.append(pre_sum[-1] + nums[i])

		cnt = {0:-1}
		for j, sj in enumerate(pre_sum):
			i = cnt.get(sj % k, j)
			if i == j:
				cnt[sj % k] = j
			elif i <= j - 2:
				return True
		return False

# 6.路径总和3
class Soliution1:
	def pathSum(self, root, targetSum):
		pre_sum = [0] * (len(root) + 1)
		for i, c in enumerate(root):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for sj in pre_sum:
			ans += cnt[sj - targetSum]
			cnt[sj] += 1
		return ans
## 灵神题解：递归二叉树的左子树和右子树
class Solution2:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1

		def dfs(node, s):
			if node is None:
				return 
			nonlocal ans
			s += node.val
			ans += cnt[s - targetSum]
			cnt[s] += 1
			dfs(node.left, s)
			dfs(node.right, s)
			cnt[s] -= 1
		dfs(root, 0)
		return ans


# 前缀和与有序集合
# 1.最小正和子数组
class Solution1:
	def minimumSumSubarray(self, nums, l, r):
		pre_sum = [nums[0]]
		for i in range(1, len(nums)):
			pre_sum.append(pre_sum[-1] + nums[i])

		ans = sum(nums)
		cnt = {0:-1}
		for j, sj in enumerate(nums):
			i = cnt.get(sj, j)
			if i == j:
				cnt[sj % ]
## 灵神题解
class Solution2:
	def minimumSumSubarray(self, nums, l, r):
		ans = inf
		s = list(accumulate(nums, intial = 0))
		sl = SortedList()
		for j in range(l, len(nums) + 1):
			sl.add(s[j - l])
			k = sl.bisect_left(s[j])
			if k:
				ans = min(ans, s[j] - sl[k - 1])
			if j >= r:
				sl.remove(s[j - r])
		return -1 if ans == inf else ans

# 距离和——排序+前缀和+二分查找
# 1.使数组元素全部相等的最少操作次数
class Solution1:  # 暴力解法
	def minOperations(self, nums, queries):
		ans = [0] * len(queries)
		for i, querie in enumerate(queries):
			ans[i] += sum(abs(x - querie) for x in nums)
		return ans
## 灵神题解
class Solution2:
	def minOperations(self, nums, queries):
		n = len(nums)
		nums.sort()
		s = list(accumulate(nums, initial = 0))  # 前缀和
		ans = []
		for q in queries:
			j = bisect_left(nums, q)
			left = q * j - s[j]
			right = s[n] - s[j] - q * (n - j)
			ans.append(left + right)
		return ans

# 2.有序数组中差绝对值之和
class Solution1:
	def getSumAbsoluteDifferences(self, nums):
		n = len(nums)
		s = list(accumulate(nums, initial = 0))
		ans = []
		for q in nums:
			j = bisect_left(nums, q)
			left = q * j - s[j]
			right = s[n] - s[j] - q * (n - j)
			ans.append(left + right)
		return ans

# 3.等值距离和
## 灵神题解：按照相同元素分组后再计算
class Solution1:
	def distance(f, nums):
		groups = defaultdict(list)
		for i, x in enumerate(nums):
			groups[x].append(i)  # 相同元素分到同一组
		ans = [0] * len(nums)
		for a in groups.values():
			n = len(a)
			s = list(accumulate(a, initial = 0))
			for j, target in enumerate(a):
				left = target * j - s[j]  # left = q * j - s[j]
				right = s[n] - s[j] - target * (n - j)  # right = s[n] - s[j] - q * (n - j)
				ans[target] = left + right
		return ans

# 前缀异或和
# 1.子数组异或查询
class Solution1:
	def xorQueries(self, arr, queries):
		ret = []
		for i in range(1, len(arr)):
			arr[i] ^= arr[i - 1]
		for left, right in queries:
			if left == 0:
				ret.append(arr[right])
			else:
				ret.append(arr[right] ^ arr[left - 1])
		return ret

class Solution2:
	def xorQueries(self, arr, queries):
		# ret = []
		pre_sum = [0] * (len(arr) + 1)
		for i in range(len(arr)):
			pre_sum[i + 1] = pre_sum[i] ^ arr[i]
		ans = []
		for left, right in queries:
			ans.append(pre_sum[right] ^ pre_sum[left - 1])
		return ans

# 2.构建回文串检测
class Solution1:
	def canMakePaliQueries(self, s, queries):
		sum = [[0] * 26]
		for c in s:
			sum.append(sum[-1].copy())
			sum[-1][ord(c) - ord('a')] += 1

		ans = []
		for left, right, k in queries:
			m = 0
			for sl, sr in zip(sum[left], sum[right + 1]):
				m += (sr - sl) % 2
			ans.append(m // 2 <= k)
		return ans
## 灵神题解优化
class Solution2:
	def canMakePaliQueries(self, s, queries):
		sum = [[0] * 26]
		for c in s:
			# 方法一：保存每种字母出现次数的奇偶性
			sum.append(sum[-1].copy())
			sum[-1][ord(c) - ord('a')] += 1
			sum[-1][ord(c) - ord('a')] %= 2 # 偶数时是0

		ans = []
		for left, right, k in queries:
			m = 0
			for sl, sr in zip(sum[left], sum[right + 1]):
				m += sr != sl
			ans.append(m // 2 <= k)
		return ans
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord('a')] ^= 1  # 奇数变偶数，偶数变奇数

        ans = []
        for left, right, k in queries:
            m = 0
            for sl, sr in zip(sum[left], sum[right + 1]):
                m += sr ^ sl
            ans.append(m // 2 <= k)
        return ans

class Solution:
    def canMakePaliQueries(self, s, queries):
        sum = [0]
        for c in s:
            bit = 1 << (ord(c) - ord('a'))
            sum.append(sum[-1] ^ bit)  # 该比特对应字母的奇偶性：奇数变偶数，偶数变奇数

        ans = []
        for left, right, k in queries:
            m = (sum[left] ^ sum[right + 1]).bit_count()
            ans.append(m // 2 <= k)
        return ans


# 1.最大的幻方
class Solution1:
	def largestMagicSquare(self, grid):
		