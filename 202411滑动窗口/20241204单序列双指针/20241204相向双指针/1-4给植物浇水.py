# 4.给植物浇水
class Solution1:
	def minimumRefill(self,plants,capacityA,capacityB):
		left,right=0,len(plants)-1
		cnt=0
		origin_A=capacityA
		origin_B=capacityB
		while left<=right:
			if left<right:
				if capacityA<plants[left]:
					cnt+=1
					capacityA=origin_A
				if capacityB<plants[right]:
					cnt+=1
					capacityB=origin_B
			else:
				if max(capacityA,capacityB)<plants[left]:
					cnt+=1

			capacityA-=plants[left]
			capacityB-=plants[right]
			left+=1
			right-=1
		return cnt
	
## 思路二：优化
class Solution2:
	def minimumRefill(self,plants,capacityA,capacityB):
		left,right=0,len(plants)-1
		cnt=0
		origin_A=capacityA
		origin_B=capacityB
		while left<right:
			if capacityA<plants[left]:
				cnt+=1
				capacityA=origin_A
			if capacityB<plants[right]:
				cnt+=1
				capacityB=origin_B
			capacityA-=plants[left]
			capacityB-=plants[right]
			left+=1
			right-=1
		if left==right and max(capacityA,capacityB)<plants[left]:
			cnt+=1
		return cnt

if __name__ == '__main__':
	plants=[2,1,1]
	capacityA=2
	capacityB=2
	s=Solution2()
	print(s.minimumRefill(plants,capacityA,capacityB))

