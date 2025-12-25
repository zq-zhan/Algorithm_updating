class Solution:
	def smallestRepunitDivByK(self, k):
		if str(k)[-1] in ('2','4','5','6','8','0'):
			return -1
		pre = 1
		while pre < 10 ** 5000:
			if pre % k == 0:
				return len(str(pre))
			else:
				pre = pre * 10 + 1
		return -1
## 灵神题解
class Solution:
	def smallestRepunitDivByK(self, k):
		seen = set()
		x = 1 % k
		while x and x not in seen:
			seen.add(x)
			x = (x * 10 + 1) % k
		return -1 if x else len(seen) + 1

if __name__ == '__main__':
	k = 24
	print(Solution().smallestRepunitDivByK(k))