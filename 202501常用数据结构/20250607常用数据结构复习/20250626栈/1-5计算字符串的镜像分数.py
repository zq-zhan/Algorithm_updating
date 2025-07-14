class Solution:
	def calculateScore(self, s):
		ans = 0
		ans_dic = defaultdict(list)
		for i, x in enumerate(s):
			position = ord(x) - ord('a')
			mirror_position = 26 - position - 1
			trans_char = chr(ord('a') + mirror_position)
			if trans_char not in ans_dic:
				ans_dic[x].append(i)
			else:
				ans += i - ans_dic[trans_char][-1]
				if len(ans_dic[trans_char]) == 1:
					del ans_dic[trans_char]
				else:
					ans_dic[trans_char].pop()
		return ans
## 灵神题解
class Solution:
	def calculateScore(self, s):
		ans = 0
		stk = [[] for _ in range(26)]
		for i, x in enumerate(map(ord, s)):
			x -= ord('a')
			if stk[25 - x]:
				ans += i - stk[25 - x].pop()
			else:
				stk[x].append(i)
		return ans
	
if __name__ == '__main__':
	s = "leetcode"
	print(Solution().calculateScore(s))