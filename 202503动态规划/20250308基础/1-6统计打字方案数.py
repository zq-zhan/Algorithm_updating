from functools import cache

class Solution1:
	def countTexts(self, pressedKeys):
		mod = (10 ** 9 + 7)
		n = len(pressedKeys)
		same_lis = []
		left = 0
		for right in range(n - 1):
			if pressedKeys[right] == pressedKeys[right + 1]:
				continue
			same_lis.append([pressedKeys[left], right - left + 1])
			left = right + 1
		same_lis.append([pressedKeys[left], n - left])
		@cache
		def dfs(i, x):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return sum(dfs(i - j, x) for j in range(1, x)) % mod

		ans = 1
		for char, num in same_lis:
			if char in ('7', '9'):
				ans = (ans * dfs(num, 5)) % mod
			else:
				ans = (ans * dfs(num, 4)) % mod
			
		return ans % mod
	
## 递推
class Solution2:
	def countTexts(self, pressedKeys):
		mod = (10 ** 9 + 7)
		n = len(pressedKeys)
		same_lis = []
		left = 0
		for right in range(n - 1):
			if pressedKeys[right] == pressedKeys[right + 1]:
				continue
			same_lis.append([pressedKeys[left], right - left + 1])
			left = right + 1
		same_lis.append([pressedKeys[left], n - left])

		ans = 1
		for char, num in same_lis:
			f = [1] + [0] * num
			for i in range(1, num + 1):
				if char in ('7', '9'):
					f[i] = sum(f[i - j] for j in range(1, 5) if i >= j) % mod
				else:
					f[i] = sum(f[i - j] for j in range(1, 4) if i >= j) % mod
			ans = (ans * f[-1]) % mod
		return ans % mod

if __name__ == '__main__':
	pressedKeys = '22233'
	print(Solution2().countTexts(pressedKeys))