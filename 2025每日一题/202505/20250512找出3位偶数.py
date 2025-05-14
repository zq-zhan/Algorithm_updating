from collections import Counter

class Solution1:
	def findEvenNumbers(self, digits):
		n = len(digits)
		ans = set()
		for i, first_num in enumerate(digits):
			if first_num % 2:
				continue
			for j in range(n):
				if j == i:
					continue
				second_num = digits[j]
				for k in range(j + 1, n):
					if k == i:
						continue
					third_num = digits[k]
					if third_num != 0:
						ans.add(third_num * 100 + second_num * 10 + first_num)
					if second_num != 0:
						ans.add(second_num * 100 + third_num * 10 + first_num)
		return sorted(list(ans))
	
class Solution2:
	def findEvenNumbers(self, digits):
		cnt_dic = Counter(digits)
		ans = []
		for i in range(100, 1000, 2):
			temp_num = Counter(map(int,str(i)))
			if all(cnt <= cnt_dic[val] for val, cnt in temp_num.items()):
				ans.append(i)
		return ans


if __name__ == '__main__':
	digits = [2,2,8,8,2]
	print(Solution2().findEvenNumbers(digits))