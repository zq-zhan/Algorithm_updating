class Solution:
	def vowelStrings(self, words):
		n = len(words)
		pre_s = [0] * (n + 1)
		for word in words:
			pre_s[i + 1] = pre_s[i] + int(word[0] in 'aeiou' and word[-1] in 'aeiou')

		ans = []
		for left, right in queries:
			ans.append(pre_s[right + 1] - pre_s[left])
		return ans

if __name__ == '__main__':
	words = ['hello', 'world', 'leetcode']
	queries = [[0, 2], [0, 1], [1, 2]]
	s = Solution()
	print(s.vowelStrings(words, queries))
