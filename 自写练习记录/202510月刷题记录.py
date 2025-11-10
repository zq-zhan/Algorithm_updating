# 20251001换水问题
class Solution:
	def numWaterBottles(self, numBottles, numExchange):
		ans = numBottles
		while numBottles >= numExchange:
			ans += numBottles // numExchange
			numBottles = numBottles // numExchange + numBottles % numExchange
		return ans

# 20251002换水问题2
class Solution:
	def maxBottlesDrunk(self, numBottles, numExchange):
		ans = numBottles
		while numBottles >= numExchange:
			numBottles -= numExchange - 1
			numExchange += 1
			ans += 1
		return ans

# 20251004盛最多水的容器
class Solution:
	def maxArea(self, height):
		ans = 0
		left, right = 0, len(height) - 1
		while left < right:
			h = min(height[left], height[right])
			ans = max(ans, h * (right - left))
			if height[left] <= height[right]:
				left += 1
			else:
				right -= 1
		return ans

# 20251008咒语和药水的成功对数
class Solution:
	def successfulPairs(self, spells, potions, success):
		potions.sort()
		ans = [0] * len(spells)
		spells = [(x, i) for i, x in enumerate(spells)]
		spells.sort(reverse = True)
		j = 0
		m = len(potions)
		for x, i in spells:
			while j < m and potions[j] * x < success:
				j += 1
			ans[i] = m - j
		return ans
## 二分查找
class Solution:
	def successfulPairs(self, spells, potions, success):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return left
		potions.sort()
		ans = []
		n = len(potions)
		for x in spells:
			ans.append(n - lower_bound(potions, success / x))
		return ans

# 20251009酿造药水需要的最少总时间
## 灵神题解
class Solution:
	def minTime(self, skill, mana):
		n = len(skill)
		s = list(accumulate(skill, initial = 0))
		start = 0
		for pre, cur in pairwise(mana):
			start += max(pre * s[i + 1] - cur * s[i] for i in range(n))
		return start + mana[-1] * s[-1]

# 20251010从魔法师身上吸取的最大能量
class Solution:
	def maximumEnergy(self, energy, k):
		ans = -inf
		n = len(energy)
		for i in range(k):
			temp_s = 0
			pre_s_mn = 0
			j = i
			while j < n:
				temp_s += energy[j]
				pre_s_mn = min(pre_s_mn, temp_s)
				j += k
			ans = max(ans, temp_s - pre_s_mn)
		return ans
## 灵神题解——后缀和
class Solution:
	def maximumEnergy(self, energy, k):
		n = len(energy)
		ans = -inf
		for i in range(n - k, n): # 枚举终点
			suf_s = accumulate(energy[j] for j in range(i, -1, -k))  # 后缀和
			ans = max(ans, max(suf_s))
		return ans
## 动态规划
class Solution:
	def maximumEnergy(self, energy, k):
		dp = [0] * (len(energy) + k)
		for i in range(k, len(energy) + k):
			dp[i] = energy[i - k] + max(dp[i - k], 0)
		return max(dp[-k:])

# 20251011施咒的最大总伤害
class Solution:
	def maximumTotalDamage(self, power):
		mx = max(power)
		new_power = [0] * (mx + 1)
		for x in power:
			new_power[x - 1] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 3) + new_power[i])
		return dfs(mx)
## 灵神题解——值域打家劫舍
class Solution:
	def maximumTotalDamage(self, power):
		cnt = Counter(power)
		a = sorted(cnt)

		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = a[i]
			j = i
			while j and a[j - 1] >= x - 2:
				j -= 1
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(len(a) - 1)

# 20251013移除字母异位词后的结果数组
class Solution:
	def removeAnagrams(self, words):
		right = 1
		while right < len(words):
			if sorted(words[right]) == sorted(words[right - 1]):
				words.pop(right)
			else:
				right += 1
		return words
## 灵神思路
class Solution:
    def removeAnagrams(self, words):
        k = 1
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):
                words[k] = t
                k += 1
        del words[k:]
        return words

# 20251014检测相邻递增子数组1
class Solution:
	def hasIncreasingSubarrays(self, nums, k):
		left = before = 0
		nums.append(-1001)
		n = len(nums)
		for right in range(1, n):
			if nums[right] > nums[right - 1]:
				continue
			if (before >= k and right - left >= k) or right - left >= 2*k:
				return True
			before = right - left
			left = right
		return False

# 20251015检测相邻递增子数组2
class Solution:
	def maxIncreasingSubarrays(self, nums):
		ans = 1
		nums.append(-inf)
		left = before = 0
		n = len(nums)
		for right in range(1, n):
			if nums[right] > nums[right - 1]:
				continue
			ans = max(ans, (right - left) // 2, min(before, right - left))
			before = right - left
			left = right
		return ans

# 20251016执行操作后的最大MEX
class Solution:
	def findSmallestInteger(self, nums, value):
		nums_dic = defaultdict(int)
		for num in nums:
			if num > 0:
				nums_dic[num % value] += 1
			else:
				pos = num + ((abs(num) - 1) // value + 1) * value
				nums_dic[pos] += 1
		ans = 0
		while nums_dic[ans % value]:
			nums_dic[ans % value] -= 1
			ans += 1
		return ans
## 灵神题解
class Solution:
	def findSmallestInteger(self, nums, value):
		cnt = Counter(x % value for x in nums)
		ans = 0
		while cnt[ans % value]:
			cnt[ans % value] -= 1
			ans += 1
		return ans
		
# 20251018执行操作后不同元素的最大数量
class Solution:
	def maxDistinctElements(self, nums, k):
		nums.sort()
		ans = 0
		pre = -inf
		for x in nums:
			temp = max(x - k, pre + 1)
			if temp <= x + k:
				ans += 1
				pre = temp
		return ans

# 22051019执行操作后字典序最小的字符串
class Solution:
	def findLexSmallestString(self, s, a, b):
		


# 20251020执行操作后的变量值
class Solution:
	def finalValueAfterOperations(self, operations):
		ans = 0
		for string in operation:
			if string[0] == '-' or string[-1] == '-':
				ans -= 1
			else:
				ans += 1
		return ans

# 20251021执行操作后元素的最高频率1
class Solution:
	def maxFrequency(self, nums, k, numOperations):
		mn, mx = min(nums), max(nums)
		n = mx - mn + 1
		m = 2 * k
		new_lis = [0] * n
		for x in nums:
			new_lis[x - mn] += 1
		pre_s = list(accumulate(new_lis))
		pre_s = [0] * k + pre_s + [pre_s[-1]] * k
		ans = max(new_lis)
		for mid in range(k, n + k):
			cnt = min(pre_s[mid + k] - pre_s[mid - k], numOperations)
			ans = max(cnt, ans)
		return ans
## 灵神题解
class Solution:
	def maxFrequency(self, nums, k, numOperations):
		cnt = defaultdict(int)
		diff = defaultdict(int)
		for x in nums:
			cnt[x] += 1
			diff[x]
			diff[x - k] += 1
			diff[x + k + 1] -= 1

		ans = sum_d = 0
		for x, d in sorted(diff.items()):
			sum_d += d
			ans = max(ans, min(sum_d, cnt[x] + numOperations))
		return ans

# 20251023判断操作后字符串中的数字是否相等1
class Solution:  # O(n^2)
	def hasSameDigits(self, s):
		s = list(map(int, s))
		while len(s) > 2:
			temp_s = ''
			n = len(s)
			for i in range(n - 1):
				temp_s += str((s[i] + s[i + 1]) % 10)
			s = list(map(int, temp_s))
		return s[0] == s[1]
## 优化
class Solution:
	def hasSameDigits(self, s):
		n = len(s) - 1
		cur = 1  # C(n - 1, 0)
		sum1, sum2 = 0, 0
		for i in range(n):
			sum1 = (sum1 + int(s[i]) * cur) % 10
			sum2 = (sum2 + int(s[i + 1]) * cur) % 10
			if i < n - 1:
				cur = cur * (n - 1 - i) // (i + 1)  # C(n - 1, 1) = C(n - 1, 0) * (n - 1 - 0) // (0 + 1)
		return sum1 == sum2

# 20251024下一个更大的数值平衡数
## 灵神题解
class Solution:
	def nextBeautifulNumber(self, n):
		while True:
			n += 1
			cnt = Counter(str(n))
			if all(int(d) == c for d, c in cnt.items()):
				return n
		
# 20251027银行中的激光束数量
class Solution:
	def numberOfBeams(self, bank):
		ans = pre = 0
		for x in bank:
			cnt = x.count('1')
			ans += pre * cnt
			if cnt > 0:
				pre = cnt
		return ans

# 20251028使数组元素等于零
class Solution:
	def countValidSelections(self, nums):
		cnt_left = 0
		s = sum(nums)
		ans = 0
		for x in nums:
			cnt_left += x
			if x == 0:
				if cnt_left == s - cnt_left:
					ans += 2
				elif abs(s - 2 * cnt_left) == 1:
					ans += 1
		return ans

# 20251029仅含置位位的最小整数
class Solution:
	def smallestNumber(self, n):
		while True:
			trans_bin = bin(n)[2:]
			if trans_bin.count('1') == len(trans_bin):
				return n
			n += 1
## 灵神题解：二进制长度为m且全为1的数为2^m - 1
class Solution:
	def smallestNumber(self, n):
		return (1 << n.bit_length()) - 1


# 20251030形成目标数组的子数组最少增加次数
class Solution:
	def minNumberOperations(self, target):
		ans = target[0]
		n = len(target)
		for i in range(1, n):
			if target[i] >= target[i - 1]:
				ans += target[i] - target[i - 1]
		return ans

# 20251031数字小镇中的捣蛋鬼
class Solution:
	def getSneakyNumbers(self, nums):
		n = len(nums) - 2
		new_arr = [0] * n
		ans = []
		for x in nums:
			if new_arr[x]:
				ans.append(x)
			if len(ans) == 2:
				return ans
			new_arr[x] += 1
## 空间O(1)做法，原地哈希，
### 通过交换让每个数字回到自己应该在的位置，如果目标位置已被相同数字占据，则该数字是重复的
class Solution:
	def getSneakyNumbers(self, nums):
		n = len(nums)
		k = n - 2
		while k < n:
			x = nums[k]
			if nums[x] == x:
				k += 1
				continue
			nums[k], nums[x] = nums[x], nums[k]
		return nums[-2:]

 