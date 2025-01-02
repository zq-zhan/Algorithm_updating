# 9.比较字符串最小字母出现频次
from bisect import bisect_left
from collections import Counter


class Solution1:
	def numSmallerByFrequency(self,queries,words):
		def f(s):
			s_set = sorted(set(s))
			s_dic = Counter(s)
			return s_dic[s_set[0]]
		ans = []
		for i, c in enumerate(words):
			words[i] = f(c)
		words.sort() 
		for x in queries:
			find = bisect_left(words, f(x) + 1)
			ans.append(len(words) - find)
		return ans
	
class Solution2:
	def numSmallerByFrequency(self, queries, words):
		def f(s):
			s_set = sorted(set(s))
			s_dic = Counter(s)
			return s_dic[s_set[0]]
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right

		for i in range(len(words)):
			words[i] = f(words[i])

		words.sort()
		ans = []
		for x in queries:
			find = lower_bound(words, f(x) + 1)
			ans.append(len(words) - find)
		return ans
	
if __name__ == '__main__':
	queries = ["bbb","cc"]
	words = ["a","aa","aaa","aaaa"]
	cls = Solution2()
	print(cls.numSmallerByFrequency(queries,words))