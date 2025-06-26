## 灵神题解——贪心
class Solution1:
	def longestSubsequence(self, s, k):
		n, m = len(s), k.bit_length()
		if n < m:
			return n
		ans = m if int(s[-m:], 2) <= k else m - 1  # int(s, 2)是将二进制转换为对应的十进制整数
		return ans + s[:-m].count('0')
## 贪心思路：所有0的个数+倒序后最大能取到的1的个数
class Solution:
	def longestSubsequence(self, s, k):
		ans = s.count('0')
		total = 0
		for i, x in enumerate(s[::-1]):
			if x == '1':
				total += 1 << i
				if total <= k:
					ans += 1
				else:
					break
		return ans
		

## 子数组
class Solution:
	def longestSubsequence(self, s, k):
		n, m = len(s), k.bit_length()
		if n < m:
			return n
		ans = m - 1
		left = 0
		temp_s = ''
		for right, x in enumerate(s):
			temp_s += x
			if right - left + 1 < m:
				continue
			while int(temp_s, 2) > k:
				temp_s = temp_s[1:]
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	

if __name__ == '__main__':
	s = "1001010"
	k = 5
	print(Solution1().longestSubsequence(s, k))