'''定长滑动窗口'''
# 1.定长子串中元音的最大数目
class Solution1:
	def maxVowels(self, s, k):
		left = ans = 0
		n = len(s)
		temp = 0
		for right, c in enumerate(s):
			while right - left + 1 < k:
				if s[right] in 'aeiou':
					temp += 1
				right += 1
			ans = max(ans, temp)
			temp -= 1 if s[left] in 'aeiou' else 0
			left += 1
		return ans
## 灵神套路：入-更新-出
class Solution2:
	def maxVowels(self, s, k):
		ans = vowels = 0
		for i, c in enumerate(s):
			if c in 'aeiou':
				vowels += 1  # 1.进入窗口
			if i < k - 1:  # 窗口大小不足k
				continue
			ans = max(ans, vowels)  # 2.更新
			if s[i - k + 1] in 'aeiou':  # 3.离开窗口
				vowels -= 1
		return ans

# 2.子数组最大平均数1
class Solution1:
	def findMaxAverage(self, nums, k):
		ans = -inf
		temp_sum = 0
		for i, c in enumerate(nums):
			temp_sum += c
			if i < k - 1:
				continue
			ans = max(ans, temp_sum/k)
			temp_sum -= nums[i - k + 1]
		return ans

# 3.大小为k且平均值大于等于阈值的子数组数目
class Solution1:
	def numOfSubarrays(self, arr, k, threshold):
		ans = 0
		temp_sum = 0
		for i, c in enumerate(arr):
			temp_sum += c
			if i < k - 1:
				continue
			# while temp_sum / k >= threshold:
			ans += 1 if temp_sum / k >= threshold else 0
			temp_sum -= arr[i - k + 1]
		return ans

# 4.半径为k的子数组平均值
class Solution1:
	def getAverages(self, nums, k):
		ans = [-1] * len(nums)
		temp_sum = 0
		for i, c in enumerate(nums):
			temp_sum += c
			if i < 2 * k:
				continue
			ans[i - k] = temp_sum // (2 * k + 1)
			temp_sum -= ans[i - 2 * k]
		return ans

# 5.得到k个黑块的最少涂色次数
class Solution1:
	def minimumRecolors(self, blocks, k):
		ans = len(blocks)
		temp_cnt = 0
		for i, c in enumerate(blocks):
			if c == 'W':
				temp_cnt += 1
			if i < k - 1:
				continue
			ans = min(ans, temp_cnt)
			if blocks[i - k + 1] == 'W':
				temp_cnt -= 1
		return ans


