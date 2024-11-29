from collections import Counter

# 每种字符至少取K个
## 方法一：自写版，逆向思维
class Solution1():
	def takeCharacters(self,s,k):
		ans=left=0
		dic_all=Counter(s)
		dic_win=Counter()
		if len(s)<3 and k>0:
			return -1
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_all['a']-dic_win['a']<k or dic_all['b']-dic_win['b']<k or dic_all['c']-dic_win['c']<k:
			# while dic_all[c]-dic_win[c]<k:
				dic_win[s[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return len(s)-ans

if __name__=='__main__':
	s="acccc"
	k=4
	print(Solution1().takeCharacters(s,k))