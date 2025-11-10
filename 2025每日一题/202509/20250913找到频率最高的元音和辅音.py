class Solution:
	def maxFreqSum(self, s):
		s = list(s)
		s.sort()
		cnt_vowels = cnt_consonant = 0
		left = 0
		for right, x in enumerate(s):
			if x == s[left]:
				continue
			if s[left] in 'aeiou':
				cnt_vowels = max(cnt_vowels, right - left)
			else:
				cnt_consonant = max(cnt_consonant, right - left)
			left = right
		if s[left] in 'aeiou':
			cnt_vowels = max(cnt_vowels, right - left + 1)
		else:
			cnt_consonant = max(cnt_consonant, right - left + 1)
		return cnt_vowels + cnt_consonant



if __name__ == '__main__':
	s = 'og'
	print(Solution().maxFreqSum(s))