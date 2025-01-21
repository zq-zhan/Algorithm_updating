from collections import Counter,defaultdict

## 字符至少出现K次的子字符串
class Solution1:
	def numberOfSubstrings(self,s,k):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(s):
			dic_win[c]+=1
			while max(dic_win.values())>=k:
				dic_win[s[left]]-=1
				left+=1
			ans+=left
		return ans
### 灵神思路:影响while条件判断的只有c因为只有c的值会增加，所以无需max
class Solution2:
	def numberOfSubstrings(self,s,k):
		ans=left=0
		dic_win=defaultdict(int)
		for right,c in enumerate(s):
			dic_win[c]+=1
			while dic_win[c]>=k:
				dic_win[s[left]]-=1
				left+=1
			ans+=left
		return ans
	
class Solution1:
	def numberOfSubstrings(self, s, k):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) >= k:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans

if __name__ == '__main__':
	s = "abacb"
	k = 2
	cls = Solution1()
	print(cls.numberOfSubstrings(s, k))