from collections import Counter

## 统计重新排列后包含另一个字符串的子字符串数目
class Solution1:
	def validSubstringCount(self,word1,word2):
		ans=left=0
		# dic_win=Counter()
		dic_word2=Counter(word2)  # 维护word2中每个字符是否已被覆盖
		for right,c in enumerate(word1):
			if c in dic_word2:
				dic_word2[c]-=1
			while max(dic_word2.values())<=0:
				if word1[left] in dic_word2:
					dic_word2[word1[left]]+=1
				left+=1
			ans+=left
		return ans

### 灵神思路（类同3-6最小覆盖子串的思路！！！）
class Solution2:
	def validSubstringCount(self,s,t):
		if len(word1)<len(t):
			return 0
		dic_word2=Counter(t)
		less=len(dic_word2)  # 串口中有less个字母的出现次数比t少
		ans=left=0
		for b in s:
			dic_word2[b]-=1
			if dic_word2[b]==0:
				less-=1
			while less==0:
				if dic_word2[s[left]]==0:
					less+=1
				dic_word2[s[left]]+=1
				left+=1
			ans+=left
		return ans


if __name__ == '__main__':
	word1="bcca"
	word2="abc"
	cls=Solution2()
	print(cls.validSubstringCount(word1,word2))