# class Slution1:
# 	def numFriendRequests(self, ages):
# 		ages.sort()
# 		ans = left = 0
# 		ori_mn = ages[0]
# 		for right, c in enumerate(nums):
# 			while c <= 0.5 * ori_mn + 7 or c >= ori_mn or 
## 注意数据范围
## 注意数据范围
class Solution2:
	def numFriendRequests(self, ages):
		cnt = [0] * 121
		for x in ages:
			cnt[x] += 1
		ans = 0
		for ax, x in enumerate(cnt):
			for ay, y in enumerate(cnt):
				if not (ay <= 0.5 * ax + 7 or ay > ax or (ay > 100 and ax < 100)):
					ans += x * (y - int(ax == ay))
		return ans
	
if __name__ == '__main__':
	ages = [16, 16]
	s = Solution2()
	print(s.numFriendRequests(ages))