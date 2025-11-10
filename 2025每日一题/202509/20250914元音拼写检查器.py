from collections import defaultdict

class Solution:
	def spellchecker(self, wordlist, queries):
		wordlen_dic = defaultdict(list)
		for word in wordlist:
			wordlen_dic[len(word)].append(word)
		ans = []
		for querie in queries:
			m = len(querie)
			target_search = wordlen_dic[len(querie)]
			temp_ans = []
			for k, target_word in enumerate(target_search):
				if target_word == querie:
					temp_ans.append((0, k, target_word))
					break
				target_word_lis = list(target_word)
				querie_lis = list(querie)
				tag_all = True
				# idx = 0
				for i in range(m):
					x = target_word_lis[i]
					y = querie_lis[i]
					if x != y:
						if x.lower() == y.lower():
							continue
						elif x in 'aeiouAEIOU' and y in 'aeiouAEIOU':
							# idx = 2
							continue
						else:
							tag_all = False
							break
				if tag_all:
					temp_ans.append((1, k, target_word))
			if temp_ans:
				temp_ans.sort()
				ans.append(temp_ans[0][2])
			else:
				ans.append('')
		return ans

	
if __name__ == '__main__':
	wordlist = ["KiTe","kite","hare","Hare"]
	queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
	s = Solution()
	print(s.spellchecker(wordlist, queries))