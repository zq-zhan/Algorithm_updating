# 5.统计已测试设备
class Solution1:
	def countTestedDevices(self, batteryPercentages):
		ans = 0
		for i, x in enumerate(batteryPercentages):
			x -= ans
			if x > 0:
				ans += 1
		return ans

if __name__ == '__main__':
	batteryPercentages = [1,1,2,1,3]
	cls = Solution1()
	print(cls.countTestedDevices(batteryPercentages))