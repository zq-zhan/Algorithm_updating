from math import inf

class Solution:
	def maximumEnergy(self, energy, k):
		ans = -inf
		n = len(energy)
		for i in range(k):
			temp_s = 0
			pre_s_mn = 0
			j = i
			while j < n:
				temp_s += energy[j]
				pre_s_mn = min(pre_s_mn, temp_s)
				j += k
			ans = max(ans, temp_s - pre_s_mn)
		return ans

if __name__ == '__main__':
	energy = [-2,-3,-1]
	k = 2
	print(Solution().maximumEnergy(energy, k))