# 7.计算字符串的镜像分数
from collections import defaultdict


class Solution1:
	def calculateScore(self, s):
		# start_a = ord('a')
		# end_z = ord('z')
		# distance = end_z - start_a + 1

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

				if len(ans_dic[trans_char]) > 1:
					# ans += ans_dic[trans_char][-1] - i
					ans_dic[trans_char].pop()
				else:
					del ans_dic[trans_char]
		return ans
	
## 灵神题解：26个栈
class Solution:
    def calculateScore(self, s):
        stk = [[] for _ in range(26)]
        ans = 0
        for i, c in enumerate(map(ord, s)):
            c -= ord('a')
            if stk[25 - c]:
                ans += i - stk[25 - c].pop()
            else:
                stk[c].append(i)
        return ans


if __name__ == '__main__':
	s = "aczzx"
	print(Solution().calculateScore(s))