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

if __name__ == '__main__':
     nums = [-3,0,1,1,2,3]
     cls=Solution2()
     print(cls.threeSum(nums))