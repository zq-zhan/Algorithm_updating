# 1.连续字符
class Solution1:
	def maxPower(self,s):
		n = len(s)
		ans = 0
		temp = 1
		for i in range(0,n):
			if i and s[i-1] == s[i]:
				temp += 1
				ans = max(ans,temp)
				continue
			ans = max(ans,temp)
			temp = 1
		return ans
# 分组循环思路(双指针思路)
class Solution2:
	def maxPower(self,s):
		res = 1
		left, right = 0, 1
		while right < len(s):
			if s[right] != s[left]:
				res = max(right - left, res)
				left = right
			right += 1
		return max(right - left, res)

# 2.哪种连续子字符串更长
class Solution1:
	def checkZeroOnes(self,s):
		long_1 = 0
		long_0 = 0
		left, right = 0, 1
		while right < len(s):
			if s[right] != s[left]:
				if s[left] == 0:
					long_0 = max(long_0, right - left)
					left = right
				else:
					long_1 = max(long_1, right - left)
			right += 1

		if s[left] == 0:
			long_0 = max(long_0, right - left)
			left = right
		else:
			long_1 = max(long_1, right - left)
		return long_1 > long_0

class Solution2:
    def checkZeroOnes(self, s):
        mx0 = mx1 = cnt = 0
        prev = '#'   
        for ch in s:
            if prev == ch:
                cnt += 1
            else:
                if prev == '0':
                    mx0 = max(mx0, cnt)
                elif prev == '1':
                    mx1 = max(mx1, cnt)
                cnt = 1
            prev = ch
        if prev == '0':
            mx0 = max(mx0, cnt)
        elif prev == '1':
            mx1 = max(mx1, cnt)
        return mx1 > mx0

# 灵神思路
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ans1 = 0
        ans0 = 0
        i= 0
        n=len(s)
        while i < n:
            start = i
            c = s[i]
            while i < n and c == s[i]:
                if s[i] == "1":
                    ans1 = max(ans1,i-start+1)
                else:
                    ans0 = max(ans0,i-start+1)
                i += 1
        return ans1 > ans0



# 3.最长的字母序连续子字符串的长度
class Soluton1:
	def longestContinuousSubstring(self,s):
		ans = 1
		left, right = 0, 1
		while right < len(s):
			temp_chr = s[right-1]
			next_chr = chr(ord(temp_chr) + 1)
			if s[right] != next_chr:
				ans = max(ans, right - left)
				left = right
			right += 1
		return max(ans, right - left)

# 4.删除字符使字符串变好
class Solution1:
	def makeFancyString(self,s):
		ans = ''
		left, right = 0, 1
		while right < len(s):
			if s[right] != s[left]:
				if right - left >= 2:
					ans += s[left] * 2
				else:
					ans += s[left]
				left = right
			right += 1
		if right - left >= 2:
			ans += s[left] * 2
		else:
			ans += s[left]
		return ans
# 灵神思路
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            start = i
            c = s[i]
            while i < n and c == s[i]:
                if (i-start+1) <3:
                    ans.append(s[i])
                i += 1
        return "".join(ans)

# 5.最长连续递增序列
class Solution1:
	def findLengthOfLCIS(self,nums):
		ans = 0
		left, right = 0, 1
		while right < len(nums):
			if s[right] <= s[right - 1]:
				ans = max(ans, right - left)
				left = right
			right += 1
		return max(ans,right - left)

# 6.最长湍流子数组
class Solution1:
	def maxTurbulenceSize(self,arr):
		ans = 1
		left, right = 0, 2
		while right < len(arr):
			if (arr[right-2] >= arr[right - 1] and arr[right - 1] >= arr[right]) or (arr[right-2] <= arr[right - 1] and arr[right - 1] <= arr[right]):
				if arr[right-2] == arr[right-1] == arr[right]:
					ans = max(ans, 1)
				else:
					ans = max(ans,right - left)
				left = right - 1
			right += 1
		if len(arr) == 1 or (len(arr) >= 2 and arr[right-2] == arr[right-1]):
			ans = max(ans, 1)
		else:
			ans = max(ans,right - left)
		return ans

# 7.股票平滑下跌阶段的数目
class Solution1:
	def getDescentPeriods(self,prices):
		ans = 0
		left, right = 0, 1
		while right < len(prices):
			if prices[right - 1] - prices[right] != 1:
				ans += (right - left) * (right - left + 1) / 2
				left = right
			right += 1
		ans += (right - left) * (right - left + 1) / 2
		return ans

# 8.汇总区间
class Solution1:
	def summaryRanges(self,nums):
		ans = []
		if len(nums) == 0:
			return ans
		left, right = 0, 1
		while right < len(nums):
			if nums[right] != nums[right - 1] + 1:
				if right - left > 1:
					ans.append(f"{nums[left]}->{nums[right - 1]}")
				else:
					ans.append(f"{nums[left]}")
				left = right
			right += 1
		if right - left > 1:
			ans.append(f"{nums[left]}->{nums[right - 1]}")
		else:
			ans.append(f"{nums[left]}")
		return ans

# 9.最长奇偶子数组
class Solution1:
	def longestAlternatingSubarray(self,nums,threshold):
		ans = 0
		left, right = 0, 1
		while right < len(nums):
			while nums[left] <= threshold and nums[left] % 2 != 0:
				left += 1
				right += 1
			if right < len(nums) and nums[right]> threshold or nums[right] % 2 == nums[right - 1] % 2:
				if nums[left] % 2 == 0 and nums[left] <= threshold:
					ans = max(ans, right - left)
				left = right
			right += 1
		if nums[left] % 2 == 0 and nums[left] <= threshold:
			ans = max(ans, right - left)
		return ans
## 灵神思路：不易错！！！
class Solution2:
	def longestAlternatingSubarray(self,nums,threshold):
		ans = i = 0
		while i < len(nums):
			if nums[i] > threshold or nums[i] % 2 != 0:
				i += 1
				continue
			start = i
			i += 1
			while i < len(nums) and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
				i += 1
			ans = max(ans, i - start)
		return ans

# 10.使元素相等的减少操作次数
'''关键是理解什么是分组循环，怎样用分组循环！！！'''
class Solution1:
	def reductionOperations(self,nums):
		nums.sort()
		ans = i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			temp = nums[start]
			while nums[i] == nums[i - 1]:
				i += 1
			nums[i] = nums[i - 1]
			ans += 1
		return ans

class Solution1:
	def reductionOperations(self,nums):
		nums.sort()
		ans = cnt = 0
		n = len(nums)
		i = 0
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] == nums[i - 1]:
				i += 1
			ans += (i - start) * cnt
			cnt += 1
		return ans
				
# 11.数组中最长的山脉
class Solution2:
	def longestMountain(self,nums):
		ans = 0
		i = 1
		n = len(nums)
		while i < n - 1:
			if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
				left = right = i
				while left > 0 and nums[left] > nums[left - 1]:
					left -= 1
				while right < n -1 and nums[right] > nums[right + 1]:
					right += 1
				# if i - left == right - i:  不一定要左右同长！
				ans = max(ans, right - left + 1)
			i += 1
		return ans


# 12.如果相邻两个颜色均相同则删除当前颜色
class Solution1:
	def winnerOfGame(self,colors):
		# colors = list(colors)
		i = 0 
		n = len(colors)
		cnt_a = 0
		cnt_b = 0
		flag = 0
		while i < n:
			start = i
			i += 1
			while colors[i] == colors[i - 1]:
				i += 1
				flag = 1
			if flag and i - start >= 3:
				if colors[start] == 'A':
					cnt_a += i - start - 2
				else:
					cnt_b += i - start - 2
			flag = 0
		if cnt_b >= cnt_a:
			return False
		else:
			return True

# 13.统计同质子字符串的数目
class Solution1:
	def countHomogenous(self,s):
		ans = i = 0
		n = len(s)
		while i < n:
			start = i
			i += 1
			while i < n and s[i] == s[i - 1]:
				i += 1
			ans += (i - start) * (i - start + 1) // 2
		return ans % (10 ** 9 + 7) 

# 14. 判断一个数组是否可以变为有序
class Solution1:
	def canSortArray(self,nums):
		i = 0
		n = len(nums)
		temp_num = 0
		while i < n:
			start = i
			i += 1
			cnt = bin(nums[start])[2:].count('1')
			while i < n and bin(nums[i])[2:].count('1') == cnt:
				i += 1
			if temp_num <= min(nums[start:i]):
				temp_num = max(nums[start:i])
			else:
				return False
		return True
# 灵神思路
class Solution2:
	def canSortArray(self,nums):
		n = len(nums)
		i = pre_max = 0
		while i < n:
			mx = 0
			start = i 
			i += 1
			ones_cnt = nums[start].bit_count()
			while i < n and nums[i].bit_count() == ones_cnt:
				if nums[i] < pre_max:
					return False
				mx = max(mx, nums[i])
				i += 1
			pre_max = mx
		return True

# 15.检测相邻递增子数组
class Solution1:
	def maxIncreasingSubarrays(self,nums):
		i = 0
		n = len(nums)
		ans = 1
		temp_lis = []
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] > nums[i - 1]:
				i += 1
			if i - start > 1:
				temp_lis.append([start,i-1])
			ans = max (ans, (i - start) // 2)
			if len(temp_lis) > 1 and start == temp_lis[-2][1] + 1:
				ans = max(ans, min(i - start, temp[-2][1] - temp[-2][0] + 1))
		return ans

class Solution1:
	def maxIncreasingSubarrays(self,nums):
		i = 0
		n = len(nums)
		ans = 1
		pre_len = 1
		while i < n:
			start = i
			i += 1
			while i < n and nums[i] > nums[i - 1]:
				i += 1
			pre_len = i - start
			ans = max (ans, (i - start) // 2, min(pre_len, i - start))  # 可以直接min是因为不是相邻那么pre_len就会是1
		return ans

# 16.使绳子变成彩色的最短时间
class Solution1:
	def minCost(self,colors,neededTime):
		i = 0
		n = len(colors)
		ans = 0
		while i < n:
			start = i
			i += 1
			while colors[i] == colors[i - 1]:
				i += 1
			if i - start > 1:
				ans += sum(colors[start:i].sort()[:-1])
		return ans

# 17.所有元音按顺序排布的最长子字符串
class Solution1:
	def longestBeautifulSubstring(self,word):
		target_dic = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
		ans = i = 0
		n = len(word)
		while i < n:
			start = i
			if word[start] != 'a':
				i += 1
				continue
			i += 1
			while word[i] in 'aeiou' and word[i] >= word[i - 1]:
				i += 1
			if len(set(word[start:i])) == 5:
				ans = max(ans, i - start)
		return ans

# 18.最长交替子数组
class Solution:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			flag = 1
			while i < n and nums[i] - nums[i - 1] == flag:
				i += 1
				flag *= (-1)
			if i - start > 1:
				ans = max(ans, i - start)
			if i < n:
				i = start + 1
			else:
				break
		return ans
## 灵神思路
class Solution2:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n - 1:
			if nums[i + 1] - nums[i] != 1:
				i += 1
				continue
			start = i
			i += 2
			while i < n and nums[i] == nums[i - 2]:
				i += 1
			ans = max(ans, i - start)
			i -= 1
		return ans
## 优化(有误)
class Solution3:
	def alternatingSubarray(self,nums):
		ans = -1
		i = 0
		n = len(nums)
		while i < n:
			start = i
			i += 1
			if start < n - 1 and nums[start + 1] - nums[start] != 1:
				i += 1
				continue
			elif start == n - 1:
				break
			flag = 1
			while i < n and nums[i] - nums[i - 1] == flag:
				i += 1
				flag *= (-1)
			ans = max(ans, i - start)
			i -= 1
		return ans

# 19.长度为k的子数组的能量值2
class Solution1:
	def resultsArray(self,nums,k):
		i = 0
		n = len(nums)
		ans = [-1] * (n - k + 1)
		for i, x in enumerate(nums):
			if i == 0 or x == nums[i - 1] + 1:
				cnt += 1
			if cnt >= k:
				ans[i - k + 1] = x
		return ans


class Solution1:
	def resultsArray(self,nums,k):
		i = 0
		n = len(nums)
		ans = []
		while i < n - k:
			start = i
			i += 1
			while i < n - k and nums[i] - nums[i - 1] == 1:
				i += 1
			if i - start >= k:
				ans[i - start - k + 1] = 
		return ans


