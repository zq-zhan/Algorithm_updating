# 1.重新分装苹果
class Solution1:
	def minimumBoxes(self, apple, capacity):
		capacity.sort(reverse = True)
		ans = 0
		for x in apple:
			while x > capacity[ans]:
				x -= capacity[ans]
				capacity[ans] = 0
				ans += 1
			capacity[ans] -= x
		return ans + 1
	
if __name__ == '__main__':
	apple = [1,3,2]
	capacity = [4, 3, 1,5, 2]
	s = Solution1()
	print(s.minimumBoxes(apple, capacity))