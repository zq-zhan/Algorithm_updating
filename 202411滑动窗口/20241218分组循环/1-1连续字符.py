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

# 分组循环思路
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
			
if __name__ == '__main__':
	# s = "leetcode"
	s = 'CCDELLLL'
	print(Solution2().maxPower(s))