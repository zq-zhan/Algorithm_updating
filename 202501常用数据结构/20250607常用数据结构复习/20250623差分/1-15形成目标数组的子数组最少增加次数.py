class Solution:
	def minNumberOperations(self, target):
		target = [0] + target
		n = len(target)
		ans = 0
		for i in range(1, n):
			ans += max(0, target[i] - target[i - 1])
		return ans
	
if __name__ == '__main__':
	target = [1,2,3,2,1]
	print(Solution().minNumberOperations(target))