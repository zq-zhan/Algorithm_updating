# 19.盛最多水的容器
class Solution1:
	def maxArea(self,height):
		n=len(height)
		area=0
		for i in range(0,n-1):
			left_x=height[i]
			j=i+1
			while j<n:
				right_y=height[j]
				area=max(area,min(left_x,right_y)*(j-i))
				j+=1
		return area
	
class Solution2:
	def maxArea(self,height):
		n=len(height)
		area=0
		left,right=0,n-1
		while left<right:
			area=max(area,min(height[left],height[right])*(right-left))
			if height[left]<height[right]:
				left+=1
			else:
				right-=1
		return area
	
if __name__ == '__main__':
	height=[1,8,6,2,5,4,8,3,7]
	s=Solution2()
	print(s.maxArea(height))