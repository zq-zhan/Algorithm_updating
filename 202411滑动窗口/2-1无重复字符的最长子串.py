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
                
                

if __name__=='__main__':
	s="pwwkew"
	cls=Solution2()
	print(cls.lengthOfLongestSubstring(s))