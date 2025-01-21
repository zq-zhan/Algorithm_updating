# 2.统计范围内的元音字符串数
class Solution1:
	def vowelStrings(self, words, queries):
		suf_vowels = [0]
		for word in words:
			cnt = 1 if word[0] in 'aeiou' and word[-1] in 'aeiou' else 0
			suf_vowels.append(suf_vowels[-1] + cnt)
		ans = []
		for left,right in queries:
			ans.append(suf_vowels[right + 1] - suf_vowels[left])
		return ans
	
if __name__ == '__main__':
	words = ["aba","bcb","ece","aa","e"]
	queries = [[0,2],[1,4],[1,1]]
	cls = Solution1()
	print(cls.vowelStrings(words, queries))