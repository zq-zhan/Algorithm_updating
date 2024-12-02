from collections import defaultdict,Counter

## 2.每个字符最多出现两次的最长子字符串
class Solution1():
	def maximumLengthSubstring(self,s):
		ans=left=0
		cnt_dic=Counter()
		for right,c in enumerate(s):
			while cnt_dic[c]>=2:
				if cnt_dic[s[left]]==0:
					del cnt_dic[s[left]]
				else:
					cnt_dic[s[left]]-=1
				left += 1
			cnt_dic[c]+=1
			ans=max(ans,right-left+1)
		return ans

class Solution_rv:
	def maximumLengthSubstring(self,s):
		ans=left=0
		dic_win=defaultdict(int)
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_win[c]>2:
				dic_win[s[left]]-=1
				left+=1
			ans=max(ans,right-left+1)
		return ans
	


if __name__=='__main__':
	s="bcbbbcba"
	cls=Solution1()
	print(cls.maximumLengthSubstring(s))