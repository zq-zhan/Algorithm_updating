# 17.所有元音按顺序排布的最长子字符串
class Solution1:
	def longestBeautifulSubstring(self,word):
		# target_dic = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
		ans = i = 0
		n = len(word)
		while i < n:
			start = i
			if word[start] != 'a':
				i += 1
				continue
			i += 1
			while i < n and word[i] in 'aeiou' and word[i] >= word[i - 1]:
				i += 1
			if len(set(word[start:i])) == 5:
				ans = max(ans, i - start)
		return ans
	
if __name__ == '__main__':
	word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
	s = Solution1()
	print(s.longestBeautifulSubstring(word))
