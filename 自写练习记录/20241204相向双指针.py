# 2.验证回文串
class Solution:
	def isPalindrome(self,s):
		left,right=0,len(s)-1
		while left<right:
			while left<right and not s[left].isalnum():  # 判断字符串是否是字母或数字
				left+=1
			while left<right and not s[right].isalnum():
				right-=1
			if s[left].lower() != s[right].lower():
				return False
			left+=1
			right-=1
		return True


# 3.删除字符串两端相同字符后的最短长度
class Solution1:
	def minimumLength(self,s):
		n=len(s)
		# ans=n
		left,right=0,n-1
		# target_char=s[0]
		while left<right and s[left]==s[right]:
			while s[left]==s[left+1] and left+1<right:
				left+=1
			while s[right]==s[right-1] and right-1>left:
				right-=1
			left+=1
			right-=1
		return right-left+1
## 思路二：
class Solution2:
	def minimumLength(self,s):
		n=len(s)
		left,right=0,len(s)-1
		while left<right and s[left]==s[right]:
			c=s[left]
			while left<=right and s[left]==c:
				left+=1
			while right>=left and s[right]==c:
				right-=1
		return right-left+1

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
class Solution1:
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

# 5.有序数组的平方
## 思路一：O(n2)
class Solution1:
	def sortedSquares(self,nums):
		for i in range(len(nums)):
			nums[i]=nums[i]**2
		return sorted(nums)
## 灵神
### 思路一：
class Solution2:
	def sortedSquares(self,nums):
		n=len(nums)
		ans_lis=[0]*n
		left,right=0,n-1
		for i in range(n-1,-1,-1):  # 排序后尾端数值的平方可能最大
			x=nums[left]*nums[left]
			y=nums[right]*nums[right]
			if x>y:
				ans_lis[i]=x
				left+=1
			else:
				ans_lis[i]=y
				right-=1
		return ans_lis
### 思路二：每次只需判断-nums[i]>nums[j]是否成立
class Solution3:
	def sortedSquares(self,nums):
		n=len(nums)
		ans=[0]*n
		left,right=0,n-1
		for i in range(n-1,-1,-1):
			x,y=nums[left],nums[right]
			if -x>y:
				ans[i]=x*x  # x*x比x**2快
				left+=1
			else:
				ans[i]=y*y
				right-=1
		return ans
class Solution:
	def sortedSquares(self,nums):
		ans=[]
		left,right=0,len(nums)-1
		while left<=right:
			a=nums[left]*nums[left]
			b=nums[right]*nums[right]
			if a<b:
				ans.append(b)
				right-=1
			else:
				ans.append(a)
				left+=1
		return ans[::-1]

# 6.找到k个最接近的元素
class Solution1:
	def findClosestElements(self,arr,k,x):
		n=len(arr)
		left,right=0,n-1
		# ans=[0]*n
		for i in range(n-1,-1,-1):
			left_x=abs(arr[left]-x)
			right_y=abs(arr[right]-x)
			if left_x<right_y or (left_x==right_y and arr[left]<arr[right]):
				ans[i]=arr[right]
				right-=1
			else:
				ans[i]=arr[left]
				left+=1
		return ans
## 灵神思路：定长滑动窗口
class Solution2:
	def findClosestElements(self,arr,k,x):
		left,right=0,len(arr)-1
		ans=[]
		while right-left+1>k:
			if abs(arr[left]-x)<=abs(arr[right]-x):
				right-=1
			else:
				left+=1
		return ans[left:right+1]

# 7.数组中的k个最强值
class Solution1:
	def getStrongest(self,arr,k):
		n=len(arr)
		left,right=0,n-1
		arr.sort()
		med=arr[(n-1)//2]
		ans=[]
		while left<=right and right-left+1>n-k:
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

# 8.两数之和-输入有序数组
class Solution1:
	def twoSum(self,numbers,target):
		n=len(numbers)
		left,right=0,n-1
		while left<right:
			temp_sum=numbers[left]+numbers[right]
			if temp_sum>target:
				right-=1
			elif temp_sum<target:
				left+=1
			else:
				return [left,right]
		return [-1,-1]

# 9.平方数之和
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

# 10.统计和小于目标的下标对数目
class Solution1:
	def countPairs(self,nums,target):
		cnt=0
		left,right=0,len(nums)-1
		while left<right and left<len(nums)-1:
			if nums[left]+nums[right]<target:
				cnt+=1
			if right-left>1:
				right-=1
			else:
				left+=1
				right=len(nums)-1
		return cnt
## 灵神思路:O(nlogn)
class Solution2:
	def countPairs(self,nums,target):
		nums.sort()
		ans=left=0
		right=len(nums)-1
		while left<right:
			if nums[left]+nums[right]<target:
				ans+=right-left
				left+=1
			else:
				right-=1
		return ans

# 11.采购方案
class Solution1:
	def purchasePlans(self,nums,target):
		nums.sort()
		left,right=0,len(nums)-1
		cnt=0
		while left<right:
			if nums[left]+nums[right]<=target:
				cnt+=right-left
				left+=1
			else:
				right-=1
		return cnt%1000000007

# 12.三数之和
class Solution1:
	def threeSum(self,nums):
		nums.sort()
		left,right=0,len(nums)-1
		ans=[]
		while left<right:
			temp_sum=nums[right]+nums[left]
			diff=-temp_sum
			if diff in nums[left+1:right]:
				temp_lis=[nums[left],diff,nums[right]]
				if temp_lis not in ans:
					ans.append(temp_lis)
					left+=1
					right-=1
					continue
			if temp_sum<0:
				left+=1
			elif temp_sum>0:
				right-=1
			else:
				left+=1
		return ans

## 灵神思路
class Solution2:
	def threeSum(self,nums):
		nums.sort()
		ans=[]
		n=len(nums)
		for i in range(n-2):
			x=nums[i]
			if i>0 and x==nums[i-1]:
				continue
			if x+nums[i+1]+nums[i+2]>0:
				break
			if x+nums[-2]+nums[-1]<0:
				continue
			j=i+1
			k=n-1
			while j < k:
				s=x+nums[j]+nums[k]
				if s > 0:
					k -= 1
				elif s < 0:
					j += 1
				else:
					ans.append([x,nums[j],nums[k]])
					j += 1
					while j < k and nums[j] == nums[j-1]:
						j += 1
					k -= 1
					while k>j and nums[k] == nums[k+1]:
						k -=1
		return ans

# 13.最接近的三数之和
class Solution1:
	def threeSumClosest(self,nums,target):
		nums.sort()
		temp_sum=inf
		n=len(nums)
		for i in range(n-2):
			x=nums[i]
			j=i+1
			k=n-1
			while j<k:
				win_sum=x+nums[j]+nums[k]
				if abs(win_sum-target)<abs(temp_sum-target):
					temp_sum=win_sum
					if win_sum-target==0:
						return temp_sum
				if win_sum<target:
					j+=1
				else:
					k-=1
		return temp_sum

## 灵神思路：添加三个优化点
class Solution2:
	def threeSumClosest(self,nums,target):
		nums.sort()
		temp_diff=inf
		n=len(nums)
		for i in range(n-2):
			x=nums[i]
			if i and x==nums[i-1]:
				continue
			s=x+nums[i+1]+nums[i+2]
			if s>target:
				if s-target<temp_diff:
					ans=s
				break
			s=x+nums[-2]+nums[-1]
			if s<target:
				if target-s<temp_diff:
					temp_diff=target-s
					ans=s
				continue
			j,k=i+1,n-1
			while j<k:
				s=x+nums[j]+nums[k]
				if s==target:
					return s
				if s>target:
					if s-target<temp_diff:
						temp_diff=s-target
						ans=s
					k-=1
				else:
					if target-s<temp_diff:
						temp_diff=target-s
						ans=s
					j+=1
		return ans


# 14.四数之和
class Solution1:  # 枚举第一个数和最后一个数
	def fourSum(self,nums,target):
		nums.sort()
		ans=[]
		n=len(nums)
		for a in range(n-3):
			if a and nums[a]==nums[a-1]:
				continue
			d=n-1
			if nums[a]+nums[-3]+nums[-2]+nums[-1]<target:
				continue
			if nums[a]+nums[a+1]+nums[a+2]+nums[a+3]>target:
				break
			while a<d:
				x1=nums[a]
				x4=nums[d]
				b=a+1
				c=d-1
				while b<c:
					s=x1+nums[b]+nums[c]+x4
					if s==target:
						ans.append([x1,nums[b],nums[c],x4])
						b+=1
						while nums[b]==nums[b-1] and b<c:
							b+=1 
						c-=1
						while nums[c]==nums[c+1] and c>b:
							c-=1
					elif s<target:
						b+=1
						# if nums[b]==nums[b-1] and b<c:
						# 	b+=1
					else:
						c-=1
						# if nums[c]==nums[c+1] and c>b:
						# 	c-=1
				d-=1
				while nums[d]==nums[d+1] and d>a:
					d-=1
		return ans
## 灵神思路
class Solution2:  # 枚举前两个数
	def fourSum(self,nums,target):
		nums.sort()
		ans=[]
		n=len(nums)
		for a in range(n-3):
			x1=nums[a]
			if a and nums[a-1]==nums[a]:
				continue
			if nums[a]+nums[-3]+nums[-2]+nums[-1]<target:
				continue
			if nums[a]+nums[a+1]+nums[a+2]+nums[a+3]>target:
				break
			for b in range(a+1,n-2):
				x2=nums[b]
				if b>a+1 and nums[b]==nums[b-1]:
					continue
				if x1+nums[b]+nums[-2]+nums[-1]<target:
					continue
				if x1+nums[b]+nums[b+1]+nums[b+2]>target:
					break
				c=b+1
				d=n-1
				while c<d:
					x3=nums[c]
					x4=nums[d]
					s=x1+x2+x3+x4
					if s==target:
						ans.append([x1,x2,x3,x4])
						c+=1
						while c<d and nums[c]==nums[c-1]:
							c+=1
						d-=1
						while d>c and nums[d]==nums[d+1]:
							d-=1
					elif s>target:
						d-=1
					else:
						c+=1
		return ans

# 15.有效三角形的个数
class Solution1:  # 超出时间限制
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for a in range(0,n-2):
			for b in range(a+1,n-1):
				c=n-1
				while c>b:
					if nums[a]+nums[b]>nums[c]:
						cnt+=c-b
						break
					else:
						c-=1
		return cnt
## 滑动窗口逻辑
class Solution2:
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for a in range(0,n-2):
			b=a+1
			c=a+2
			while c<n:
				if nums[a]+nums[b]>nums[c]:
					cnt+=c-b
					c+=1
				elif b<c-1:
					b+=1
				else:
					c+=1
		return cnt
	
# 灵神思路一：固定较大的指针
class Solution3:
	def triangleNumber(self,nums):
		nums.sort()
		cnt=0
		n=len(nums)
		for c in range(2,n):
			a=0
			b=c-1
			while a<b:
				if nums[a]+nums[b]>nums[c]:
					cnt+=b-a  # 向右移动a都成立
					b-=1
				else:
					a+=1
		return cnt

class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for k in range(2, len(nums)):
            c = nums[k]
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] > c 同时意味着：
                    # nums[i+1]+nums[j] > c
                    # nums[i+2]+nums[j] > c
                    # ...
                    # nums[j-1]+nums[j] > c
                    # 从 i 到 j-1 一共 j-i 个
                    ans += j - i
                    j -= 1
                else:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] <= c 同时意味着
                    # nums[i]+nums[j-1] <= c
                    # ...
                    # nums[i]+nums[i+1] <= c
                    # 所以在后续的内层循环中，nums[i] 不可能作为三角形的边长，没有用了
                    i += 1
        return ans

# 16.数的平方等于两数乘积的方法数
class Solution1:
	def numTriplets(self,nums1,nums2):
		def count_cnt(nums,target_nums):
			nums.sort()
			nums_dic=Counter(nums)
			n=len(nums)
			cnt=0
			for i in range(len(target_nums)):
				target_sum=target_nums[i]*target_nums[i]
				left,right=0,n-1
				while left<right:
					temp_sum=nums[left]*nums[right]
					if temp_sum<target_sum:
						left+=1
					elif temp_sum>target_sum:
						right-=1
					else:
						if nums[left]!=nums[right]:
							cnt+=nums_dic[nums[left]]*nums_dic[nums[right]]
						else:
							cnt+=nums_dic[nums[left]]*(nums[left]-1)/2
						left+=1
						right-=1
						while nums[left]==nums[left-1] and left<right:
							left+=1
						right-=1
						while nums[right]==nums[right+1] and left<right:
							right-=1
			return cnt
		type1_cnt=count_cnt(nums1,nums2)
		type2_cnt=count_cnt(nums2,nums1)
		return type1_cnt+type2_cnt


class Solution2:
	def numTriplets(self,nums1,nums2):
		cnt=0
		nums1_dic=Counter(nums1)
		nums2_dic=Counter(nums2)
		nums1_set=list(set(nums1))
		nums2_set=list(set(nums2))
		nums1_set.sort()
		nums2_set.sort()
		for x in nums1_set:
			left=0
			right=len(nums2_set)-1
			while left<right:
				if nums2_set[left]*nums2_set[right]==x**x:
					cnt+=nums2_dic[nums2_set[left]]*nums2_dic[nums2_set[right]]*nums1_dic[x]
					left+=1
					right-=1
				elif nums2_set[left]*nums2_set[right]<x**2:
					left+=1
				else:
					right-=1
			for y in nums2_dic.keys():
				if nums2_dic[y]>1:
					if x==y:
						cnt+=nums2_dic[y]*(nums2_dic[y]-1)/2*nums1_dic[x]


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
		return int(cnt%(10**9+7))
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

# 18.令牌放置
class Solution1:
	def bagOfTokensScore(self,token,power):
		token.sort()
		n=len(token)
		left,right=0,n-1
		ans=0
		max_ans=0
		while left<=right:
			if power>=token[left]:
				power-=token[left]
				ans+=1
				left+=1
				max_ans=max(max_ans,ans)
			else:
				if ans>0:
					power+=token[right]
					ans-=1
					right-=1
				else:
					break
		return max_ans

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

