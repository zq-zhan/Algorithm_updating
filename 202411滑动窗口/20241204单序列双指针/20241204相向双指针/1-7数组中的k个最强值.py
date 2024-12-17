# 7.数组中的k个最强值
## 思路一：复杂度：O(nlogn)
class Solution1:
	def getStrongest(self,arr,k):
		n=len(arr)
		left,right=0,n-1
		arr.sort()
		med=arr[(n-1)//2]
		ans=[]
		while right-left+1>n-k:
			if abs(arr[left]-med)>abs(arr[right]-med):
				ans.append(arr[left])
				left+=1
			else:
				ans.append(arr[right])
				right-=1
		return ans
# 思路二：
class Solution2:
	def getStrongest(self,arr,k):
		n=len(arr)
		left,right=0,n-1
		arr.sort()
		med=arr[(n-1)//2]
		ans=[]
		while len(ans)<k:
			if abs(arr[left]-med)>abs(arr[right]-med):
				ans.append(arr[left])
				left+=1
			else:
				ans.append(arr[right])
				right-=1
		return ans


if __name__=='__main__':
	arr=[6,7,11,7,6,8]
	k=5
	s=Solution1()
	print(s.getStrongest(arr,k))