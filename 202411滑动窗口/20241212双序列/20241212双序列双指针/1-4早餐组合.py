# 4.早餐组合
class Solution1:
	def breakfastNumber(self,staple,drink,x):
		staple.sort()
		drink.sort()
		n = len(staple)
		m = len(drink)
		p1, p2 = n-1, m-1
		ans=0
		while p1 >= 0:
			while p2 >= 0:
				if staple[p1] + drink[p2] <= x:
					ans += (p2+1)
					break
				p2 -= 1
			p1 -= 1
			p2 = m-1
		return ans
	
class Solution2:
	def breakfastNumber(self,staple,drink,x):
		staple.sort()
		drink.sort()
		n = len(staple)
		m = len(drink)
		p1, p2 = 0, m-1
		ans=0
		while p1 < n and p2 >=0:
			if staple[p1]+drink[p2]<=x:
				ans += (p2+1)
				p1 += 1
			else:
				p2 -= 1
		return ans%(1000000007)

if __name__ == '__main__':
	staple = [10,11,5]
	drink = [5,5,2]
	x = 15
	s = Solution2()
	print(s.breakfastNumber(staple,drink,x))