# 8.统计重新排列后包含另一个字符串的子字符串数目1
from collections import Counter

class Solution1:
	def validSubstringCount(self, word1, word2):
		word2_dic = Counter(word2)
		# word2_dic_copy = word2_dic.copy()
		left = right = 0
		n = len(word1)
		ans = 0
		while right < n and left < n:
			if word1[right] in word2:
				word2_dic[word1[right]] -= 1
				# right += 1
			while max(word2_dic.values()) <= 0:
				ans += n - right
				word2_dic[word1[left]] += 1 if word1[left] in word2 else 0
				left += 1
			right += 1
		return ans
	
## 统计重新排列后包含另一个字符串的子字符串数目
class Solution2:
	def validSubstringCount(self,word1,word2):
		ans=left=0
		dic_win=Counter()
		dic_word2=Counter(word2)
		for right,c in enumerate(word1):
			if c in dic_word2:
				dic_word2[c]-=1
			while max(dic_word2.values())<=0:
				if word1[left] in dic_word2:
					dic_word2[word1[left]]+=1
				left+=1
			ans+=left
		return ans


if __name__ == '__main__':
	# word1 = 'dcbdcdccb'
	# word2 = 'cdd'
	word1 = 'abcabc'
	word2 = 'abc'
	cls = Solution2()
	print(cls.validSubstringCount(word1, word2))