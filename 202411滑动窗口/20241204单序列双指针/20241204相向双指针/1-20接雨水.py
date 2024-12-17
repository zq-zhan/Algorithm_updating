# 20.接雨水
class Solution1:
	def trap(self,height):
		n=len(height)
		area=0
		left=0
		right=1
		temp=0
		while left<right:
			if height[left]>height[right]:
				temp+=height[right]
				right+=1
			else:
				area+=height[left]*(right-left)-temp
				temp=0
				left=right
				right+=1
		return area
## 灵神思路
class Solution2:
	def trap(self,height):
		ans=left=pre_max=suf_max=0
		right=len(height)-1
		while left<right:
			pre_max=max(pre_max,height[left])
			suf_max=max(suf_max,height[right])
			if pre_max<suf_max:
				ans+=pre_max-height[left]
				left+=1
			else:
				ans+=suf_max-height[right]
				right-=1
		return ans
	
if __name__ == '__main__':
	height=[0,1,0,2,1,0,1,3,2,1,2,1]
	clas=Solution2()
	print(clas.trap(height))