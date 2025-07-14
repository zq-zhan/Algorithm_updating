class Solution:
	def strWithout3a3b(self, a, b):
		ans = ''
		while a > 0 or b > 0:
			if a > b:
				if b > 0:
					ans += 'a' * min(a, 2) + 'b'
				else:
					ans += 'a' * min(a, 2)
				a -= min(a, 2)
				b -= 1
			elif a == b:
				if ans and ans[-1] == 'a':
					ans += 'b' * min(a, 2) + 'a' * min(b, 2)
				else:
					ans += 'a' * min(a, 2) + 'b' * min(b, 2)
				a -= min(a, 2)
				b -= min(b, 2)
			else:
				if a > 0:
					ans += 'b' * min(b, 2) + 'a'
				else:
					ans += 'b' * min(b, 2)
				a -= 1
				b -= min(b, 2)
		return ans

	
if __name__ == '__main__':
	a = 3
	b = 4
	print(Solution().strWithout3a3b(a, b))