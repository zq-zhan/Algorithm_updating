# 2.通过删除字母匹配到字典里最长的单词
class Solution1:
	def findLongestWord(self,s,dictionary):
		ans = ''
		for word in dictionary:
			p1 = p2 = 0
			n, m = len(s), len(word)
			while p1 < n and p2 < m:
				if s[p1] != word[p2]:
					p1 += 1
				else:
					p2 += 1

			if p2 == m and len(word) >= len(ans):
				temp = word
				if word<temp:
					ans = word
		return ans
	
if __name__ == '__main__':
	s = "abpcplea"
	dictionary = ['a','b','c']
	print(Solution1().findLongestWord(s,dictionary))