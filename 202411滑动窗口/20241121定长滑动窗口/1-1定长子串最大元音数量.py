# 方法一：暴力解法
class Solution1:
	def maxVowels(self,s,k):
		res=0
		for i in range(len(s)-k+1):
			substr=s[i:i+k]
			dic={'a':0,'e':0,'i':0,'o':0,'u':0}
			for x in substr:
				if x in dic.keys():
					dic[x]+=1
			res=max(res,sum(dic.values()))
		return res

# 方法二：滑动窗口
class Solution2():
	def maxVowels(self,s,k):
		ans=vowel=0
		for i,c in enumerate(s):
			if c in "aeiou":
				vowel+=1
			if i < k-1:
				continue
			ans=max(ans,vowel)
			if s[i-k+1] in "aeiou":
				vowel-=1
		return ans


## 20241201复习
class Solution4:
	def maxVowels(self,s,k):
		ans=cnt=0
		for i,c in enumerate(s):
			cnt+=1 if c in "aeiou" else 0
			if i < k-1:  # 注意这里的符号
				continue
			ans=max(ans,cnt)
			cnt-=1 if s[i-k+1] in "aeiou" else 0
		return ans

# 1.定长子串中元音的最大数目
class Solution5:
	def maxVowels(self, s, k):
		left = ans = 0
		# n = len(s)
		temp = 0
		for right, c in enumerate(s):
			while right - left + 1 < k:
				if s[right] in 'aeiou':
					temp += 1
				right += 1
			ans = max(ans, temp)
			temp -= 1 if s[left] in 'aeiou' else 0
			left += 1


s="abciiidef"
k=3
cls=Solution5()
print(cls.maxVowels(s,k))