from collections import Counter

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
                

if __name__=='__main__':
	s="abcabcbb"
	cls=Solution_rv()
	print(cls.lengthOfLongestSubstring(s))