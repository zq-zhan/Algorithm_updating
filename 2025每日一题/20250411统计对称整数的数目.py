class Solution1:
	def countSymmetricIntegers(self, low, high):
		ans = 0
		for x in range(low, high + 1):
			x = str(x)
			if len(x) % 2 == 0:
				mid = len(x) // 2
				left = 0
				right = 0
				for i, c in enumerate(x):
					if i < mid:
						left += int(c)
					else:
						right += int(c)
				ans += int(left == right)
		return ans

## 灵神思路
class Solution2:
	def countSymmetricIntegers(self, low, high):
		ans = 0
		for x in range(low, high + 1):
			x = str(x)
			mid = len(x) // 2
			if len(x) % 2 == 0 and sum(map(ord, x[:mid])) == sum(map(ord, x[mid:])):
				ans += 1
		return ans
	
if __name__ == '__main__':
	low = 1200
	high = 1230
	print(Solution2().countSymmetricIntegers(low, high))