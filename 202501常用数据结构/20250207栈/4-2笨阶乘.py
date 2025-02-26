# 2.笨阶乘
class Solution1:
	def clumsy(self, n):
		num_lis = [i for i in range(n, 0, -1)]
		st = []
		ans = 0
		for i, c in enumerate(num_lis):
			if (i + 1) % 4 == 0:
				ans += c
			else:
				st.append(c)

			if len(st) < 3:
				continue
			else:
				temp_result = int(st[-3] * st[-2] / st[-1])
				if ans == 0:
					ans += temp_result
				else:
					ans -= temp_result
				st = []

		# temp_result = 1
		# for x in st:
		# 	temp_result *= x

		# if len(st) == 1:
		# 	ans -= 1
		# elif len(st) == 2:
		# 	ans -= 2
		return ans - len(st)
	

## 思路二：优化 
class Solution2:
	def clumsy(self, n):
		cnt = 0
		st = [n]
		for i in range(n - 1, 0, -1):
			if cnt % 4 == 0:
				st.append(st.pop() * i)
			elif cnt % 4 == 1:
				st.append(int(st.pop() / i))
			elif cnt % 4== 2:
				st.append(i)
			elif cnt % 4== 3:
				st.append(-i)
			cnt += 1
		return sum(st)

	
if __name__ == '__main__':
	n = 10
	s = Solution2()
	print(s.clumsy(n))