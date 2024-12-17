# 9.平方数之和
from math import isqrt, sqrt


class Solution1:
	def judgeSquareSum(self,c):
		target_num=int(sqrt(c))
		left,right=0,target_num
		while left<=right:
			if left*left+right*right==c:
				return True
			elif left*left+right*right>c:
				right-=1
			else:
				left+=1
		return False
	
## 灵神思路一：
class Solution2:
	def judgeSquareSum(self,c):
		a=0
		while a*a*2<=c:
			b=isqrt(c-a*a)
			if a*a+b*b==c:
				return True
			a+=1
		return False
	
if __name__=='__main__':
	c=3
	s=Solution2()
	print(s.judgeSquareSum(c))