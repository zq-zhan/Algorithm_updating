class Solution:
	def minNumberOperations(self, target):
		ans = target[0]
		n = len(target)
		for i in range(1, n):
			if target[i] >= target[i - 1]:
				ans += target[i] - target[i - 1]
		return ans


if __name__ == '__main__':
	target = [3,1,1,2]
	print(Solution().minNumberOperations(target))