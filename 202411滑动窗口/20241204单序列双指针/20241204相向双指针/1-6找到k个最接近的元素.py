# 6.找到k个最接近的元素
class Solution1:  # 错误
	def findClosestElements(self,arr,k,x):
		n=len(arr)
		left,right=0,n-1
		ans=[0]*n
		for i in range(0,n,1):
			left_x=abs(arr[left]-x)
			right_y=abs(arr[right]-x)
			if left_x<right_y or (left_x==right_y and arr[left]<arr[right]):
				ans[i]=arr[left]
				left+=1
			else:
				ans[i]=arr[right]
				right-=1
		return sorted(ans[:k])

## 灵神思路
class Solution2:
	def findClosestElements(self,arr,k,x):
		left,right=0,len(arr)-1
		# ans=[]
		while left<right and right-left+1>k:
			if abs(arr[left]-x)<=abs(arr[right]-x):
				right-=1  # 先排除最不接近的元素，缩小窗口
			else:
				left+=1
		return arr[left:right+1]

if __name__=='__main__':
	arr=[0,0,1,2,3,3,4,7,7,8]
	k=3
	x=5
	cls=Solution1()
	print(cls.findClosestElements(arr,k,x))