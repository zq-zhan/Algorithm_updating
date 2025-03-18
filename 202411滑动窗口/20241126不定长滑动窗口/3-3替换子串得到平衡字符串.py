from collections import Counter

# 替换子串得到平衡字符串
## 方法一：自写版
class Solution1:
	def balancedString(self,s):
		ans=len(s)+1
		left=0
		target_num=len(s)//4
		dic_all=Counter(s)
		if len(dic_all)==4 and min(dic_all.values())==target_num:
			return 0
		for right,c in enumerate(s):
			dic_all[c]-=1
			while max(dic_all.values())<=target_num:
				dic_all[s[left]]+=1
				ans=min(ans,right-left+1)
				left += 1
		return ans 


class Solution1:
	def balancedString(self, s):
		ans = 0
		left = 0
		n = len(s)
		dic_all = {'Q':0, 'E':0, 'W':0, 'R':0}
		for x in s:
			dic_all[x] += 1
		for x in 'QWER':
			while dic_all[x] > n // 4:
				ans += 1
				dic_all[x] -= 1
				if dic_all['Q'] < n // 4:
					dic_all['Q'] += 1
				elif dic_all['E'] < n // 4:
					dic_all['E'] += 1
				elif dic_all['W'] < n // 4:
					dic_all['W'] += 1
				elif dic_all['R'] < n // 4:
					dic_all['R'] += 1
		return ans

## 灵神题解
class Solution2:
	def balancedString(self, s):
		m = len(s) // 4
		cnt = Counter(s)
		if len(cnt) == 4 and min(cnt.values()) == m:
			return 0

		ans = len(s) + 1
		left = 0
		for right, c in enumerate(s):
			cnt[c] -= 1
			while max(cnt.values()) <= m:
				ans = min(ans, right - left + 1)
				cnt[s[left]] += 1
				left += 1
		return ans


class Solution3:  # 错解——是替换子串、所以无法用贪心思路求解
	def balancedString(self, s):
		s_dic = Counter(s)
		m = len(s) // 4
		ans = 0
		for value in s_dic.values():
			ans += value - m if value > m else 0
		return ans

class Solution4:  
	def balancedString(self, s):
		s_dic = Counter(s)
		m = len(s) // 4
		if len(s_dic) == 4 and min(s_dic.values()) == m:
			return 0

		ans = len(s)
		left = 0
		for right, c in enumerate(s):
			s_dic[c] -= 1
			while max(s_dic.values()) <= m:
				ans = min(ans, right - left + 1)
				s_dic[s[left]] += 1
				left += 1
		return ans 
	
if __name__ == '__main__':
	s = "WWEQERQWQWWRWWERQWEQ"
	print(Solution4().balancedString(s))