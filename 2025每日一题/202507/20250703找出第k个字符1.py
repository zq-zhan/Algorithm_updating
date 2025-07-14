class Solution:
	def kthCharacter(self, k):
		ord_a = ord('a')
		ans = 'a'
		while len(ans) < k:
			n = len(ans)
			for i in range(n):
				ans += chr((ord(ans[i]) - ord_a + 1) % 26 + ord_a)
				if len(ans) == k:
					return ans[-1]
		return ans[-1]

if __name__ == '__main__':
	s = Solution()
	print(s.kthCharacter(10))