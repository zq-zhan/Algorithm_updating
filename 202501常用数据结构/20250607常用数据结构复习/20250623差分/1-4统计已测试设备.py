class Solution:
	def countTestedDevices(self, batteryPercentages):
		ans = 0
		cnt = 0
		for x in batteryPercentages:
			if x - cnt > 0:
				ans += 1
				cnt += 1
		return ans
	
if __name__ == '__main__':
	batteryPercentages = [1, 1, 2, 1, 3]
	print(Solution().countTestedDevices(batteryPercentages))