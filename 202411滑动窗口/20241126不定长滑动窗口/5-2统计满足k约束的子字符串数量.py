## 统计满足k约束的子字符串数量
from collections import defaultdict


class Solution1:
	def countKConstraintSubstrings(self,s,k):
		ans=left=0
		dic_win={'0':0,'1':0}
		for right,c in enumerate(s):
			dic_win[c]+=1
			while min(dic_win.values())>k:
				dic_win[s[left]]-=1
				left+=1
			ans+=right-left+1
		return ans

class Solution1:
	def countKConstraintSubstrings(self, s, k):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while min(dic_win.values()) > k:
				dic_win[s[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans

if __name__=='__main__':
	s="11111"
	k=1
	print(Solution1().countKConstraintSubstrings(s,k))