from collections import Counter

# 17.三数之和的多种可能
class Solution1:
	def threeSumMulti(self,arr,target):
		arr.sort()
		arr_dic=Counter(arr)
		cnt=0
		n=len(arr)
		for i in range(0,n-2):
			if arr[i]==arr[i-1] and i:
				continue
			x1=arr[i]
			j=i+1
			k=n-1
			while j<k:
				x2=arr[j]
				x3=arr[k]
				s=x1+x2+x3
				if s<target:
					j+=1
				elif s>target:
					k-=1
				else:
					if x1==x2==x3:
						temp=arr_dic[x1]
						cnt+=temp*(temp-1)*(temp-2)/6
					elif x1==x2!=x3:
						temp=arr_dic[x1]
						cnt+=temp*(temp-1)/2*arr_dic[x3]
					elif x1==x3!=x2:
						temp=arr_dic[x1]
						cnt+=temp*(temp-1)/2*arr_dic[x2]
					elif x1!=x2==x3:
						temp=arr_dic[x2]
						cnt+=temp*(temp-1)/2*arr_dic[x1]
					else:
						cnt+=arr_dic[x1]*arr_dic[x2]*arr_dic[x3]
					j+=1
					while arr[j]==arr[j-1] and j<k:
						j+=1
					k-=1
					while arr[k]==arr[k+1] and k>j:
						k-=1
		return int(cnt%(1000000000+7))

## 思路二：
class Solution2:
	def threeSumMulti(self,arr,target):
		if len(arr)<3:
			return 0
		arr.sort()
		cnt=0
		for i in range(len(arr)):
			left=i+1
			right=len(arr)-1
			while left<right:
				s=arr[i]+arr[left]+arr[right]
				if s>target:
					right-=1
				elif s<target:
					left+=1
				else:
					t1=1
					t2=1
					if arr[left]==arr[right]:
						cnt+=(right-left+1)*(right-left)/2
						break
					while arr[left]==arr[left+1] and left+1<=right:
						t1+=1
						left+=1
					while arr[right]==arr[right-1] and right-1>=left:
						t2+=1
						right-=1
					cnt+=t1*t2
					left+=1
					right-=1
		return int(cnt%(10**9+7))


if __name__=='__main__':
    arr=[1,1,2,2,2,2]
    target=5
    s=Solution2()
    print(s.threeSumMulti(arr,target))