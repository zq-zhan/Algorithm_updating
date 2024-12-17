from collections import Counter

## 统计好子数组的数目
class Solution1:
	def countGood(self,nums,k):
		ans=left=0
		total=0
		dic_win=Counter()
		for right,c in enumerate(nums):
			dic_win[c]+=1
			if dic_win[c]>=2:
				total+=(dic_win[c]-1)
			while total>=k:
				# if dic_win[s[left]]==1:
				# 	del dic_win
				total-=(dic_win[nums[left]]-1) if dic_win[nums[left]]>=2 else 0
				dic_win[nums[left]]-=1
				left+=1
			ans+=left
		return ans

if __name__ == '__main__':
	nums=[1,1,1,1,1]
	k=10
	cls=Solution1()
	print(cls.countGood(nums,k))