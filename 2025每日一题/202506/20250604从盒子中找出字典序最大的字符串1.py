class Solution1:
	def answerString(self, word, numFriends):
		if numFriends == 1:
			return word
		n = len(word)
		target_len = n - numFriends + 1
		ans = ''
		for i in range(n):
			ans = max(ans, word[i:i + target_len])
		return ans
## 灵神题解
class Solution:
    def answerString(self, s, numFriends):
        if numFriends == 1:
            return s
        n = len(s)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        return s[i: i + n - numFriends + 1]

if __name__ == '__main__':
	word = "aann"
	numFriends = 2
	print(Solution().answerString(word, numFriends))