class Solution:
	def lengthOfLongestSubstring(self,s):
		dic,res,i={},0,-1
		for j in range(len(s)):
			if s[j] in dic:
				i=max(dic[s[j]],i)
			dic[s[j]]=j
			res=max(res,j-i)
		return res

# 方法二：
class Solution2():
	def getLongestSubstring(self, s):
		res=0
		for length in range(1,len(s)+1):
			for i in range(len(s)-length+1):
				string=s[i:i+length]
				dict={}
				flag=True
				for char in string:
					if char in dict:
						flag=False
						break
					dict[char]=1
				if flag:
					res=max(res,length)
					break
		return res

s="abba"

cls=Solution()
print(cls.lengthOfLongestSubstring(s))