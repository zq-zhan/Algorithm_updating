class Solution:
	def sortVowels(self, s):
		s = list(s)
		temp_lis = []
		temp_index = []
		for i, x in enumerate(s):
			if x in 'aeiouAEIOU':
				temp_lis.append(x)
				temp_index.append(i)
		temp_lis.sort()
		for i, index in enumerate(temp_index):
			s[index] = temp_lis[i]
		return ''.join(s)
	
if __name__ == '__main__':
	s = "lEetcOde"
	print(Solution().sortVowels(s))