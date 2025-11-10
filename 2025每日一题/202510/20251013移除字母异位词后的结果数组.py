from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2,s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Solution:
	def removeAnagrams(self, words):
		right = 1
		while right < len(words):
			if sorted(words[right]) == sorted(words[right - 1]):
				words.pop(right)
			else:
				right += 1
		return words

class Solution:
    def removeAnagrams(self, words):
        k = 1
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):
                words[k] = t
                k += 1
        del words[k:]
        return words

if __name__ == '__main__':
	words = ["abba","baba","bbaa","cd","cd"]
	print(Solution().removeAnagrams(words))