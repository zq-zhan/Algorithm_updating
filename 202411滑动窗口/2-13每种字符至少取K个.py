from collections import Counter

# 每种字符至少取K个
## 方法一：自写版，逆向思维
class Solution1():
	def takeCharacters(self,s,k):
		ans=left=0
		dic_all=Counter(s)
		dic_win=Counter()
		if any(dic_all[c]<k for c in 'abc'):
			return -1
		for right,c in enumerate(s):
			dic_win[c]+=1
			# while dic_all['a']-dic_win['a']<k or dic_all['b']-dic_win['b']<k or dic_all['c']-dic_win['c']<k:
			while dic_all[c]-dic_win[c]<k:
				dic_win[s[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return len(s)-ans

## 方法二：灵神滑动窗口
class Solution2():
	def takeCharacters(self,s,k):
		ans=left=0
		dic_all=Counter(s)
		if any(dic_all[c]<k for c in 'abc'):
			return -1
		for right,c in enumerate(s):
			dic_all[c] -= 1
			while dic_all[c] < k:  # 窗口之外的c不足k
				dic_all[s[left]] += 1
				left += 1
			ans = max(ans,right-left+1)
		return len(s)-ans


if __name__=='__main__':
	s="acccc"
	k=4
	print(Solution2().takeCharacters(s,k))