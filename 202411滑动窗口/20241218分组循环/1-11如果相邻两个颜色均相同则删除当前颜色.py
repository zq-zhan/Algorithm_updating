# 12.如果相邻两个颜色均相同则删除当前颜色
class Solution1:
	def winnerOfGame(self,colors):
		# colors = list(colors)
		i = 0 
		n = len(colors)
		cnt_a = 0
		cnt_b = 0
		flag = 0
		while i < n:
			start = i
			i += 1
			while colors[i] == colors[i - 1]:
				i += 1
				flag = 1
			if flag and i - start >= 3:
				if colors[start] == 'A':
					cnt_a += i - start - 2
				else:
					cnt_b += i - start - 2
			flag = 0
		if cnt_b >= cnt_a:
			return False
		else:
			return True



if __name__ == '__main__':
	colors = "ABBBBBBBAAA"
	cls = Solution1()
	print(cls.winnerOfGame(colors))