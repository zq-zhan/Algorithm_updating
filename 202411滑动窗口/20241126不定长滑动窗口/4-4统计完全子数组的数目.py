from collections import Counter

## 统计完全子数组的数目
class Solution1:
	def countCompleteSubarrays(self,nums):
		ans=left=0
		dic_all=Counter(nums)
		dic_win=Counter()
		n=len(dic_all)
		for right,c in enumerate(nums):
			dic_win[c]+=1
			while len(dic_win)==n:
				if dic_win[nums[left]]==1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]]-=1
				left+=1
			ans+=left
		return ans
	
if __name__=='__main__':
	nums=[459,459,962,1579,1435,756,1872,1597]
	s=Solution1()
	print(s.countCompleteSubarrays(nums))