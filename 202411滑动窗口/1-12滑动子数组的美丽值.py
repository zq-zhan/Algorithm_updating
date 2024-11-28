## 12.滑动子数组的美丽值
### 方法一：自写版，超出时间限制
class Solution1():
	def getSubarrayBeauty(self,nums,k,x):
		ans_lis=[]
		substr_lis=[]
		for i,c in enumerate(nums):
			substr_lis.append(c)
			if i < k-1:
				continue
			sort_lis=sorted(substr_lis)
			if sort_lis[x-1]<0:
				ans_lis.append(sort_lis[x-1])
			else:
				ans_lis.append(0)
			substr_lis=substr_lis[1:]
		return ans_lis
### 方法二：灵神
class Solution2():
	def getSubarrayBeauty(self,nums,k,x):
		cnt_lis=[0]*101
		for c in nums[:k-1]:
			cnt_lis[c]+=1
		ans_lis=[0]*(len(nums)-k+1)
		for i,(in_,out) in enumerate(zip(nums[k-1:],nums)):
			cnt_lis[in_]+=1
			left=x
			for j in range(-50,0):
				left -= cnt_lis[j]
				if left <=0:
					ans_lis[i]=j
					break
			cnt_lis[out]-=1
		return ans_lis

if __name__ == '__main__':
	nums=[1,-1,-3,-2,3]
	k=3
	x=2
	s2=Solution2()
	print(s2.getSubarrayBeauty(nums,k,x))