class Solution:
	def compareVersion(self, version1, version2):
		version1 = list(version1.split('.'))
		version2 = list(version2.split('.'))
		while int(version1[-1]) == 0:
			version1.pop()
		while int(version2[-1]) == 0:
			version2.pop()
		n, m = len(version1), len(version2)
		i = j = 0
		while i < n and j < m:
			x = int(version1[i])
			y = int(version2[j])
			if x == y:
				i += 1
				j += 1
				continue
			elif x < y:
				return -1
			else:
				return 1
		if i == n and j == m:
			return 0
		elif i < n and j == m:
			return 1
		else:
			return -1

if __name__ == '__main__':
	version1 = "1.0"
	version2 = "1.0.0.0"
	s = Solution()
	print(s.compareVersion(version1, version2))