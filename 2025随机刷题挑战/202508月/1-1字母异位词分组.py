from collections import defaultdict

class Solution:
	def groupAnagrams(self, strs):
		ans_dic = defaultdict(list)
		ord_a = ord('a')
		for substr in strs:
			res = []
			for x in substr:
				res.append(str(ord(x) - ord_a))
			res.sort()
			res = ''.join(res)
			ans_dic[res].append(substr)
		ans = []
		for _, value in ans_dic.items():
			ans.append(value)
		return ans
	
if __name__ == '__main__':
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(Solution().groupAnagrams(strs))