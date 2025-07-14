class Solution:
	def buildArray(self, target, n):
		ans = []
		temp_ans = []
		for i in range(1, n + 1):
			if i in target:
				temp_ans.append(i)
				ans.append('Push')
			else:
				if target == temp_ans:
					break
				else:
					ans.append('Push')
					ans.append('Pop')
		return ans
	
if __name__ == '__main__':
	target = [1, 3]
	n = 3
	print(Solution().buildArray(target, n))