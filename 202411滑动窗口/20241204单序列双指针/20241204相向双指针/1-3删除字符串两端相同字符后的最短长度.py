# 删除字符串两端相同字符后的最短长度
class Solution1:
	def minimumLength(self,s):
		n=len(s)
		# ans=n
		left,right=0,n-1
		# target_char=s[0]
		while left<right and s[left]==s[right]:
			while s[left]==s[left+1] and left+1<right:
				left+=1
			while s[right]==s[right-1] and right-1>left:
				right-=1
			left+=1
			right-=1
		return right-left+1

## 思路二：
class Solution2:
	def minimumLength(self,s):
		n=len(s)
		left,right=0,len(s)-1
		while left<right and s[left]==s[right]:
			c=s[left]
			while left<=right and s[left]==c:
				left+=1
			while right>=left and s[right]==c:
				right-=1
		return right-left+1


if __name__ == "__main__":
	# s="aabccabba"
	s="cabaabac"
	cls=Solution2()
	print(cls.minimumLength(s))