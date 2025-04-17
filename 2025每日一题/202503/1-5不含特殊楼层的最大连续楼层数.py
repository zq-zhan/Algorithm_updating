# 5.不含特殊楼层的最大连续楼层数
class Solution1:
	def maxConsecutive(self, bottom, top, special):
		new_arr = [bottom - 1] + special + [top + 1]
		new_arr.sort()
		ans = 0
		for i in range(1, len(new_arr)):
			ans = max(ans, new_arr[i] - new_arr[i - 1] - 1)
		return ans

	
if __name__ == '__main__':
	bottom = 2
	top = 9
	special = [4, 6]
	s = Solution1()
	print(s.maxConsecutive(bottom, top, special))