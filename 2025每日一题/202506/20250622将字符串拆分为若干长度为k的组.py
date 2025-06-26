class Solution:
	def divideString(self, s, k, fill):
		left = 0
		ans = []
		temp_s = ''
		for right, x in enumerate(s):
			temp_s += x
			if right - left + 1 < k:
				continue
			ans.append(temp_s)
			left = right + 1
			temp_s = ''
		if left < len(s):
			ans.append(temp_s + fill * (k - right + left - 1))
		return ans
	
## 灵神题解
class Solution:
	def divideString(self, s, k, fill):
		# n = len(s)
		# return [s[i:i + k] + fill * (k - n + i) for i in range(0, n, k)]
		## 先补全
		while len(s) % k != 0:
			s += fill
		return [s[i:i + k] for i in range(0, len(s), k)]
	
if __name__ == '__main__':
	s = "abcdefghij"
	k = 3
	fill = "x"
	print(Solution().divideString(s, k, fill))