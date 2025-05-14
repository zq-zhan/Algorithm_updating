from collections import defaultdict

class Solution1:
	def countOfSubstrings(self, word, k):
		dic_yuan1 = defaultdict(int)
		dic_yuan2 = defaultdict(int)
		cnt_fu1 = cnt_fu2 = ans = left1 = left2 = 0
		for right, c in enumerate(word):
			if c in "aeiou":
				dic_yuan1[c] += 1
				dic_yuan2[c] += 1
			else:
				cnt_fu1 += 1
				cnt_fu2 += 1
			while len(dic_yuan1) == 5 and cnt_fu1 >= k:
				if word[left1] in "aeiou":
					if dic_yuan1[word[left1]] == 1:
						del dic_yuan1[word[left1]]
					else:
						dic_yuan1[word[left1]] -= 1
				else:
					cnt_fu1 -= 1
				left1 += 1
			while len(dic_yuan2) == 5 and cnt_fu2 >= k + 1:
				if word[left2] in "aeiou":
					if dic_yuan2[word[left2]] == 1:
						del dic_yuan2[word[left2]]
					else:
						dic_yuan2[word[left2]] -= 1
				else:
					cnt_fu2 -= 1
				left2 += 1
			ans += left1 - left2
		return ans
	
if __name__ == '__main__':
	word = "aeiou"
	k = 0
	print(Solution1().countOfSubstrings(word, k))