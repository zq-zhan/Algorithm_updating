class Solution1:
	def countGoodTriplets(self, arr, a, b, c):
		ans = 0
		n = len(arr)
		for j in range(1, n - 1):
			for i in range(0, j):
				if abs(arr[i] - arr[j]) > a:
					continue
				for k in range(j + 1, n):
					if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
						ans += 1
					else:
						continue
		return ans
	
if __name__ == '__main__':
	arr = [3,0,1,1,9,7]
	a = 7
	b = 2
	c = 3
	print(Solution1().countGoodTriplets(arr, a, b, c))