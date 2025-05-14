################### 单序列双指针 #############
# 1.反转字符串
class Solution1:
	def reverseString(self, s):
		n = len(s)
		left, right = 0, n - 1
		while left < right:
			s[left], s[right] = s[right], s[left]
			left += 1
			right -= 1
		return s

# 2.验证回文串
class Solution1:
	def isPalindrome(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not s[left].isalnum():
				left += 1
			while left < right and not s[right].isalnum():
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True

# 3.删除字符串两端相同字符后的最短长度
class Solution1:
	def minimumLength(self, s):
		n = len(s)
		left, right = 0, n - 1
		while left < right:
			if s[left] != s[right]:
				break
			while left + 1 < right and s[left] == s[left + 1]:
				left += 1
			while left < right - 1 and s[right] == s[right - 1]:
				right -= 1
			left += 1
			right -= 1
		return right - left + 1

# 4.给植物浇水
class Solution1:
	def minimumRefill(self, plants, capacityA, capacityB):
		n = len(plants)
		ans = 0
		left, right = 0, n - 1
		curA = capacityA
		curB = capacityB
		while left <= right:
			if left < right:
				if plants[left] <= curA:
					curA -= plants[left]
				else:
					ans += 1
					curA = capacityA - plants[left]

				if plants[right] <= curB:
					curB -= plants[right]
				else:
					ans += 1
					curB = capacityB - plants[right]
			else:
				if max(curA, curB) < plants[left]:
					ans += 1
			left += 1
			right -= 1
		return ans

# 5.有序数组的平方
class Solution1:
	def sortedSquares(self, nums):
		n = len(nums)
		left, right = 0, n - 1
		ans = [0] * n
		for p in range(n - 1, -1, -1):
			x = nums[left] ** 2
			y = nums[right] ** 2
			if x <= y:
				ans[p] = y
				right -= 1
			else:
				ans[p] = x
				left += 1
		return ans

# 6.找到K个最接近的元素
class Solution1:
	def findClosestElements(self, arr, k, x):
		n = len(arr)
		left, right = 0, n - 1
		while right - left + 1 > k:
			a = nums[left]
			b = nums[right]
			if abs(a - x) > abs(b - x):
				left += 1
			elif abs(a - x) < abs(b - x):
				right -= 1
			else:
				right -= 1
		return arr[left: right + 1]

# 7.数组中K个最强值
class Solution1:
	def getStrongest(self, arr, k):
		n = len(arr)
		arr.sort()
		mid = arr[(n - 1) // 2]
		left, right = 0, n - 1
		ans = []
		# for _ in range(n):
		# 	# if len(ans) < k:
		# 	a = abs(arr[left] - mid)
		# 	b = abs(arr[right] - mid)
		# 	if b >= a:
		# 		ans.append(arr[right])
		# 		right -= 1
		# 	else:
		# 		ans.append(arr[left])
		# 		left += 1
		# 	if len(ans) < k:
		# 		continue
		# 	else:
		# 		return ans
		while len(ans) < k:
			if abs(arr[right] - mid) >= abs(arr[left] - mid):
				ans.append(arr[right])
				right -= 1
			else:
				ans.append(arr[left])
				left += 1
		return ans

# 8.两数之和2-输入有序数组
class Solution1:
	def twoSum(self, numbers, target):
		n = len(numbers)
		left, right = 0, n - 1
		while left < right:
			if numbers[left] + numbers[right] < target:
				left += 1
			elif numbers[left] + numbers[right] > target:
				right -= 1
			else:
				return [left + 1, right + 1]

# 9.平方数之和
class Solution1:
	def judgeSquareSum(self, c):
		left, right = 0, int(sqrt(c))
		while left <= right:
			if left ** 2 + right ** 2 > c:
				right -= 1
			elif left ** 2 + right ** 2 < c:
				left += 1
			else:
				return True
		return False

# 10.统计和小于目标的下标对数目
class Solution1:
	def countPairs(self, nums, target):
		nums.sort()
		n = len(nums)
		left, right = 0, n - 1
		ans = 0
		while left < right:
			if nums[left] + nums[right] < target:
				ans += right - left
				left += 1
			else:
				right -= 1
		return ans

# 11.统计公平数对的数目
class Solution1:
	def countFairPairs(self, nums, lower, upper):
		ans = 0
		for i, c in enumerate(nums):
			for j in range(i + 1, len(nums)):
				if lower <= c + nums[j] <= upper:
					ans += 1
		return ans
## 灵神题解
### 二分查找
class Solution3:
	def countFairPairs(self, nums, lower, upper):
		nums.sort()
		ans = 0
		for j, x in enumerate(nums):
			r = bisect_right(nums, upper - x, 0, j)
			l = bisect_left(nums, lower - x, 0, j)
			ans += r - l
		return ans
## 关键：排序不影响答案——加法交换律
class Solution4:  # O(nlogn)
	def countFairPairs(self, nums, lower, upper):
		nums.sort()
		def count(target):
			temp_ans = 0
			left, right = 0, len(nums) - 1
			while left < right:
				if nums[left] + nums[right] <= target:
					temp_ans += right - left
					left += 1
				else:
					right -= 1
			return temp_ans
		return count(upper) - count(lower - 1) 

# 12.采购方案
class Solution1:
	def purchasePlans(self, nums, target):
		mod = 10 ** 9 + 7
		nums.sort()
		ans = 0
		left, right = 0, len(nums) - 1
		while left < right:
			if nums[left] + nums[right] <= target:
				ans += right - left
				left += 1
			else:
				right -= 1
		return ans % mod
		
# 13.数的平方等于两数乘积的方法数
class Solution1:
	def numTriplets(self, nums1, nums2):
		def upper(nums, target):
			nums.sort()
			ans = 0
			left, right = 0, len(nums) - 1
			while left < right:
				if nums[left] * nums[right] <= target:
					ans += right - left 
					left += 1
				else:
					right -= 1
			return ans

		ans_result = 0
		for x in nums1:
			ans_result += upper(nums2, x ** 2) - upper(nums2, x ** 2 - 1)
		for y in nums2:
			ans_result += upper(nums1, y ** 2) - upper(nums1, y ** 2 - 1)
		return ans_result

# 14.接雨水
class Solution1:  # 超时
	def trap(self, height):
		target_set = sorted(set(height))
		ans = 0
		temp_height = height.copy()
		left, right = 0, len(height) - 1
		for target in target_set:
			
			while left < right:
				while left < right and height[left] < target:
					left += 1
				while left < right and height[right] < target:
					right -= 1
				if left < right:
					break
			for i in range(left + 1, right):
				if temp_height[i] < target:
					ans += target - temp_height[i]
					temp_height[i] = target
		return ans
## 灵神题解
class Solution:
    def trap(self, height):
        ans = left = pre_max = suf_max = 0
        right = len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans		

# 15.分割两个字符串得到回文串
class Solution1:
	def checkPalindromeFormation(self, a, b):
		pre_str_a = sub_str_a = pre_str_b = sub_str_b = ""
		left, right = 0, len(a) - 1
		mid = len(a) // 2
		while left < right:
			pre_str_a += a[left]
			sub_str_a += a[right]
			pre_str_b += b[left]
			sub_str_b += b[right]
			left += 1
			right -= 1
			if len(pre_str_a) > 1 and pre_str_a != sub_str_b and pre_str_b != sub_str_a:
				return False
		return True

class Solution:
    def checkPalindromeFormation(self, a, b):
        # 如果 a_prefix + b_suffix 可以构成回文串则返回 True，否则返回 False
        def check(a: str, b: str) -> bool:
            i, j = 0, len(a) - 1  # 相向双指针
            while i < j and a[i] == b[j]:  # 前后缀尽量匹配
                i += 1
                j -= 1
            s, t = a[i: j + 1], b[i: j + 1]  # 中间剩余部分
            return s == s[::-1] or t == t[::-1]  # 判断是否为回文串
        return check(a, b) or check(b, a)

# 16.最接近的三数之和
class Solution1:
	def threeSumClosest(self, nums, target):
		nums.sort()
		ans = inf
		for i, c in enumerate(nums[:-2]):
			left, right = i + 1, len(nums) - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if abs(temp_s - target) < abs(ans - target):
					ans = temp_s
				if temp_s == target:
					return target:
				elif temp_s < target:
					left += 1
				else:
					right -= 1
		return ans
		
# 17.三数之和
class Solution1:
	def threeSum(self, nums):
		ans = set()
		n = len(nums)
		nums.sort()
		for i, c in enumerate(nums[:-2]):
			left, right = i + 1, n - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if temp_s == 0:
					temp_ans = (c, nums[left], nums[right])
					ans.add(temp_ans)
					left += 1
				elif temp_s < 0:
					left += 1
				else:
					right -= 1
		return [list(val) for val in ans]
## 优化：提前判断 去重
class Solution2:
	def threeSum(self, nums):
		ans = []
		n = len(nums)
		nums.sort()
		for i, c in enumerate(nums[:-2]):
			if i > 0 and nums[i - 1] == c:
				continue
			left, right = i + 1, n - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if temp_s == 0:
					ans.append([c, nums[left], nums[right]])
					left += 1
					while left < right and nums[left] == nums[left - 1]:
						left += 1
					while left < right and nums[right - 1] == nums[right]:
						right -= 1
					right -= 1
				elif temp_s < 0:
					left += 1
				else:
					right -= 1
		return ans

# 18.四数之和
class Solution1:
	def fourSum(self, nums, target):
		nums.sort()
		n = len(nums)
		ans = []
		for i in range(n - 3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, n - 2):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue
				left, right = j + 1, n - 1
				while left < right:
					temp_s = nums[i] + nums[j] + nums[left] + nums[right]
					if temp_s < target:
						left += 1
					elif temp_s > target:
						right -= 1
					else:
						ans.append([nums[i], nums[j], nums[left], nums[right]])
						right -= 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
		return ans

# 19.有效三角形的个数
class Solution1:
	def triangleNumber(self, nums):
		nums.sort()
		ans = 0
		n = len(nums)
		for k in range(2, n):
			left, right = 0, k - 1
			while left < right:
				if nums[left] + nums[right] > nums[k]:
					ans += right - left  # 以right为第二条边的合法三角形个数
					right -= 1
				else:
					left += 1  # 保证单调性
		return ans

# 20.三数之和的多种可能
class Solution1:
	def threeSumMulti(self, arr, target):
		arr.sort()
		mod = 10 ** 9 + 7
		ans = 0

		def upper(i, target):
			temp_ans = 0
			left, right = i + 1, len(arr) - 1
			while left < right:
				if arr[i] + arr[left] + arr[right] <= target:
					temp_ans += right - left
					left += 1
				else:
					right -= 1
			return temp_ans

		for i in range(len(arr) - 2):
			ans += upper(i, target) - upper(i, target - 1)
		return ans % mod

# 21.令牌放置
class Solution1:
	def bagOfTokensScore(self, tokens, power):
		tokens.sort()
		ans = temp_ans = 0
		left, right = 0, len(tokens) - 1
		while left <= right:
			if power >= tokens[left]:
				temp_ans += 1
				ans = max(ans, temp_ans)
				power -= tokens[left]
				left += 1
			elif temp_ans > 0:
				temp_ans -= 1
				power += tokens[right]
				right -= 1
			else:
				return ans
		return ans

# 22.满足条件的子序列数目
class Solution1:
	def numSubseq(self, nums, target):
		mod = 10 ** 9 + 7
		nums.sort()
		ans = 0
		left, right = 0, len(nums) - 1
		while left <= right:
			if nums[left] + nums[right] <= target:
				ans += 2 ** (right - left)  # 以left最小元素
				left += 1
			else:
				ans += 1 if nums[right] * 2 <= target else 0
				right -= 1
		return ans % mod




#################### 同向双指针 ################
# 1.有效三角形的个数
class Solution1:  # O(n^2)
	def triangleNumber(self, nums):
		nums.sort()  # 排序后枚举最大的边
		n = len(nums)
		ans = 0
		for right in range(n - 1, 1, -1):
			c = nums[right]
			for left in range(right - 1, 0, -1):
				b = nums[left]
				for k in range(left):
					if nums[k] + b > c:
						ans += left - k
						break
		return ans
## 
class Solution2:
	def triangleNumber(self, nums):
		nums.sort()  # 排序后枚举最大的边
		n = len(nums)
		ans = 0
		for k in range(2, n):
			left, right = 0, k - 1
			while left < right:
				if nums[left] + nums[right] > nums[k]:
					ans += right - left 
					right -= 1
				else:
					left += 1
		return ans