from collections import Counter, defaultdict

class Solution1():
	def lengthOfLongestSubstring(self,s):
		ans=0
		dic=Counter()
		substr=''
		for i,c in enumerate(s):
			if c not in substr:
				substr+=c
				dic[substr]+=1
				continue
			ans=max(ans,len(substr))
			substr=substr[1:]+c
		return ans
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        for length in range(1,len(s)+1):
            dic=Counter()
            for i in range(len(s)-length+1):
                string=s[i:i+length]
                if len(set(string))==len(string):
                    ans=max(ans,len(set(string)))
        return ans
            
# 不定长滑动窗口——求最长/最大
## 20241202复习
class Solution_rv:
	def lengthOfLongestSubstring(self,s):
		ans=left=0
		dic_win=Counter()
		for right,c in enumerate(s):
			dic_win[c]+=1
			while max(dic_win.values())>1:
				dic_win[s[left]]-=1
				left += 1
			ans=max(ans,right-left+1)
		return ans

# 1、无重复字符的最长子串
class Solution5:
	def lengthOfLongestSubstring(self, s):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			if max(dic_win.values()) <= 1:
				continue
			ans = max(ans, len(dic_win))
			dic_win[s[left]] -= 1
			left += 1
		return ans

class Solution6:
	def lengthOfLongestSubstring(self, s):
		temp_win = set()
		left, right = 0, 0
		n = len(s)
		ans = 0
		while right < n:
			while left <= right and s[right] in temp_win:
				temp_win.remove(s[left])
				left += 1
			temp_win.add(s[right])
			ans = max(ans, right - left + 1)
			right += 1
		return ans

if __name__=='__main__':
	s="abcabcbb"
	cls=Solution6()
	print(cls.lengthOfLongestSubstring(s))