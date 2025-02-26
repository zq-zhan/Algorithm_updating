class Solution1:
	def buildArray(self, target, n):
		ans = []
		max_num = min(n + 1, target[-1] + 1)
		for i in range(1, max_num):
			if i in target:
				ans.append('Push')
			else:
				ans.extend(['Push','Pop'])
		return ans

				
if __name__ == '__main__':
	cls = Solution1()
	target = [1,3]
	n = 5
	print(cls.buildArray(target, n))