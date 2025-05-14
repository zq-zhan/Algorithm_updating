# 7.数组中K个最强值
class Solution1:
	def getStrongest(self, arr, k):
		n = len(arr)
		arr.sort()
		mid = arr[(n - 1) // 2]
		left, right = 0, n - 1
		ans = [0] * n
		for i in range(n):
			a = abs(arr[left] - mid)
			b = abs(arr[right] - mid)
			if b >= a:
				ans[i] = arr[right]
				right -= 1
			else:
				ans[i] = arr[left]
				left += 1
		return ans[:k]
	
class Solution2:
	def getStrongest(self, arr, k):
		n = len(arr)
		arr.sort()
		mid = arr[(n - 1) // 2]
		left, right = 0, n - 1
		ans = []
		for _ in range(n):
			a = abs(arr[left] - mid)
			b = abs(arr[right] - mid)
			if b >= a:
				ans.append(arr[right])
				right -= 1
			else:
				ans.append(arr[left])
				left += 1
			if len(ans) < k:
				continue
			else:
				return ans

if __name__ == '__main__':
	arr = [513]
	k = 1
	print(Solution2().getStrongest(arr, k))