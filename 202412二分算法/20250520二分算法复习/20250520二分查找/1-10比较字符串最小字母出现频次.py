from collections import Counter

class Solution1:
	def numSmallerByFrequency(self, queries, words):
		def f(substr):
			substr = list(substr)
			substr.sort()
			ans = 1
			for i in range(1, len(substr)):
				if substr[i] == substr[i - 1]:
					ans += 1
				else:
					break
			return ans

		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		queries = [f(querie) for querie in queries]
		words = [f(word) for word in words]
		words.sort()
		ans = []
		for target in queries:
			ans.append(len(words) - lower_bound(words, target + 1))
		return ans



if __name__ == '__main__':
	queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
	words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
	print(Solution1().numSmallerByFrequency(queries, words))