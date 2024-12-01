from collections import Counter
from math import inf

# 最小覆盖子串
## 方法一：自写版
class Solution1:
	def minWindow(self,s,t):
		ans=inf
		left=0
		# dic_win=Counter()
		t_dic=Counter(t)
		result_substr=''
		for right,c in enumerate(s):
			if t_dic[c]>0:
				if t_dic[c]==1:
					del t_dic[c]
				else:
					t_dic[c]-=1
			while len(t_dic)==0:
				if right-left+1<ans:
					result_substr=s[left:right+1]
					ans=min(ans,right-left+1)
				if s[left] in t:
					t_dic[s[left]]+=1
				left+=1
		return result_substr
	
class Solution2:
	def minWindow(self,s,t):
		ans=inf
		left=0
		dic_win=Counter()
		t_dic=Counter(t)
		result_substr=''
		for right,c in enumerate(s):
			if c in t:
				dic_win[c]+=1
			while len(dic_win)==len(t_dic):  #无法解决数量的问题
				ans=min(ans,right-left+1)
				result_substr=s[left:right+1]
				if dic_win[s[left]]>0:
					if dic_win[s[left]]==1:
						del dic_win[s[left]]
					else:
						dic_win[s[left]]-=1
				left+=1
		return result_substr


class Solution_true:
	def minWindow(self,s,t):
		ans=inf
		left=0
		dic_win=Counter()
		t_dic=Counter(t)
		result_substr=''
		less=len(t_dic)  # 维护目标字符串中是否都满足至少的个数
		for right,c in enumerate(s):
			dic_win[c]+=1
			if dic_win[c]==t_dic[c]:  # 易错点1:>的时候和==的时候都满足，并不影响less不同种字符是否都满足的计算
				less-=1
			while less==0:
				if ans>right-left+1:
					ans=min(ans,right-left+1)
					result_substr=s[left:right+1]
				if t_dic[s[left]]==dic_win[s[left]]:
					less+=1
				dic_win[s[left]]-=1
				left+=1
		return result_substr


if __name__=='__main__':
	s="ADOBECODEBANC"
	t='ABC'
	print(Solution_true().minWindow(s,t))