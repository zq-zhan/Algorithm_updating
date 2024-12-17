from collections import Counter

# 16.数的平方等于两数乘积的方法数
class Solution1:
	def numTriplets(self,nums1,nums2):
		# n1=len(nums1)
		# n2=len(nums2)
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
							cnt+=nums_dic[nums[left]]*(nums_dic[nums[left]]-1)/2
						left+=1
						right-=1
						while nums[left]==nums[left-1] and left<right:
							left+=1
						# right-=1
						while nums[right]==nums[right+1] and left<right:
							right-=1
						# left+=1
						# right-=1
						# if left and nums[left]==nums[left-1]:
						# 	cnt+=1
						# 	left+=1
						# if right<n-1 and nums[right]==nums[right+1]:
						# 	cnt+=1
						# 	right-=1
			return cnt
		type1_cnt=count_cnt(nums1,nums2)
		type2_cnt=count_cnt(nums2,nums1)
		return int(type1_cnt+type2_cnt)
	
if __name__=='__main__':
	nums1=[1,1]
	nums2=[1,1,1]
	s=Solution1()
	print(s.numTriplets(nums1,nums2))