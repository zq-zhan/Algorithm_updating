from collections import Counter, defaultdict

# class Solution:
# 	def findAnagrams(self, s, p):
# 		dic_p = Counter(p)
# 		temp_win = dic_p.copy()
# 		ans = []
# 		left = 0
# 		for right, x in enumerate(s):
# 			if x not in dic_p:
# 				temp_win = dic_p.copy()
# 				left = right + 1
# 				continue
# 			elif not temp_win[x]:
# 				temp_win = dic_p.copy()
# 				left = right
# 			temp_win[x] -= 1
# 			if max(temp_win.values()) == 0:
# 				ans.append(left)
# 				temp_win[s[left]] += 1
# 				left += 1
# 		return ans
	
# class Solution:
# 	def findAnagrams(self, s, p):
# 		dic_p = Counter(p)
# 		ans = []
# 		k = len(p)
# 		# n = len(s)
# 		temp_win = defaultdict(int)
# 		for i, x in enumerate(s):
# 			temp_win[x] += 1
# 			if sum(temp_win.values()) == k:
# 				if temp_win == dic_p:
# 					ans.append(i - k + 1)
# 				if temp_win[s[i - k + 1]] == 1:
# 					del temp_win[s[i - k + 1]]
# 				else:
# 					temp_win[s[i - k + 1]] -= 1
# 		return ans

# 请使用 Python3 提交代码！Python2 已经被淘汰了
class Solution:
    def findAnagrams(self, s, p):
        ans = []
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口
            left = right - len(p) + 1
            if left < 0:  # 窗口长度不足 len(p)
                continue
            if cnt_s == cnt_p:  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
            cnt_s[s[left]] -= 1  # 左端点字母离开窗口
        return ans


if __name__ == '__main__':
	s = "cbaebabacd"
	p = "abc"
	print(Solution().findAnagrams(s, p))