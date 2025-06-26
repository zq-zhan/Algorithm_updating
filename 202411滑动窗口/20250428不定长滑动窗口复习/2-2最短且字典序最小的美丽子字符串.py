class Solution1:
	def shortestBeautifulSubstring(self, s, k):
		ans = s + '0'
		left = cnt = 0
		temp_s = ''
		for right, c in enumerate(s):
			temp_s += c
			cnt += int(c == '1')
			while cnt == k:
				if len(ans) > len(temp_s) or (len(ans) == len(temp_s) and ans > temp_s):
					ans = temp_s
				temp_s = temp_s[1:]
				cnt -= int(s[left] == '1')
				left += 1
		return ans if ans != s + '0' else ''
	
if __name__ == '__main__':
	s = "100011001"
	k = 3
	print(Solution1().shortestBeautifulSubstring(s, k))