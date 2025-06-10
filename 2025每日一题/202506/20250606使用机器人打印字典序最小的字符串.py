class Solution:
	def robotWithString(self, s):
		mn = s[0]
		cnt = 1
		for i in range(1, len(s)):
			if s[i] < mn:
				cnt = 1
				mn = s[i]
			elif s[i] == mn:
				cnt += 1
			else:
				continue

		ans = ''
		for i in range(len(s)):
			if s[i] == mn:
				if cnt == 1:
					ans += s[i]
					break
				else:
					ans += s[i]
					cnt -= 1
			else:
				ans += s[i]
		return ans[::-1] + s[i + 1:]
	
if __name__ == '__main__':
	s = "baac"
	print(Solution().robotWithString(s))